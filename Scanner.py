from lib.midi_file import MidiFile
from lib.messages.message import *
from lib.messages.data import *
from lib.track import Track
from lib.messages.event import MidiEvent
from lib.meta_messages.meta_message import *
from lib.meta_messages.meta_data import *
from lib.meta_messages.meta_event import *

FILE_HEADER = '4D 54 68 64 00 00 00 06'
TRACK_HEADER = '4D 54 72 6B'
TRACK_TAIL = 'FF 2F 00'
META_MESSAGE_LEADER = 'FF'

class Scanner:
    def __init__(self, data: 'list[int]'):
        self.data = data
        self.ptr = 0

    def parse(self):
        return self.parse_file()
    
    def parse_file(self):
        self.validate_and_consume(hex_string_to_bytes(FILE_HEADER))
        format = bytes_to_int(self.consume(2))
        track_count = bytes_to_int(self.consume(2))
        ticks_per_crotchet = bytes_to_int(self.consume(2))

        tracks = []

        while self.ptr < len(self.data):
            tracks.append(self.parse_track())

        return MidiFile(format, track_count, ticks_per_crotchet, tracks)
    
    def parse_track(self):
        events = []
        track_complete = False
        if self.peek(4) == hex_string_to_bytes(TRACK_HEADER):
            self.validate_and_consume(hex_string_to_bytes(TRACK_HEADER))

            track_length = self.consume_to_int(4)

            while not track_complete:
                event = self.parse_event()
                events.append(event)
                track_complete = type(event.message) is TrackCompleteMessage

            return Track(track_length, events)
        else:
            raise Exception(f"{hex(self.peek(4))} at position {self.ptr} is not a valid track header.{self.context()}")
        
    def parse_event(self):
        delta_time = self.parse_delta_time()
        message = self.parse_message()

        if message is MetaMessage:
            return MetaEvent(delta_time, message)

        return MidiEvent(delta_time, message)

    def parse_delta_time(self):
        sum = 0
        next_digit = self.consume_to_int(1)
        while (next_digit & 0b10000000 > 0): # Last digit of the delta time has 0 in the most significant position
            sum = (sum << 7) + (self.data[self.ptr] & 0b01111111) # We ignore that first bit
            next_digit = self.consume_to_int(1)
        
        final = (sum << 7) + (next_digit & 0b01111111)
        return final
    
    def parse_message(self) -> MidiMessage:
        message_leader = self.consume_to_int(1)
        if message_leader == hex_string_to_bytes(META_MESSAGE_LEADER)[0]:
            return self.parse_meta_message()
        
        message_type = message_leader >> 4 # The four most significant bits are the message type
        channel = message_leader & 0b1111 # The last four are the channel

        # The spec uses hex representation, so we match with that for convenience
        match message_type:
            case 0x8: return NoteOnMessage(channel, NoteData(self.consume_to_int(1), self.consume_to_int(1)))
            case 0x9: return NoteOffMessage(channel, NoteData(self.consume_to_int(1), self.consume_to_int(1)))
            case 0xA: return KeyAfterTouchMessage(channel, NoteData(self.consume_to_int(1), self.consume_to_int(1)))
            case 0xB: return ControlChangeMessage(channel, ControlChangeData(self.consume_to_int(1), self.consume_to_int(1)))
            case 0xC: return ProgramChangeMessage(channel, ProgramChangeData(self.consume_to_int(1)))
            case 0xD: return ChannelPressureMessage(channel, ChannelPressureData(self.consume_to_int(1)))
            case 0xE: 
                # The first bit of each is 0 and is dropped
                byte1 = self.consume_to_int(1)
                if (byte1 & 0b10000000 != 0):
                    raise Exception(f"The first byte of PitchWheelChange message was non-zero at {self.ptr}.{self.context()}")

                byte2 = self.consume_to_int(1)
                if (byte2 & 0b10000000 != 0):
                    raise Exception(f"The first byte of PitchWheelChange message was non-zero at {self.ptr}.{self.context()}")

                data = (byte1 << 7) | byte2

                return PitchWheelChangeMessage(channel, data)
            case _: raise Exception(f"Message leader {hex(message_leader)} is invalid.{self.context()}")
        
    def parse_meta_message(self):
        meta_message_leader = self.consume_to_int(1)

        match meta_message_leader:
            case 0x0: return SetSeqNumberMessage(SetSeqNumberData(self.consume_to_int(1), self.consume_to_int(2))) # Always 2 bytes
            case 0x1: return self.consume_text_metadata(TextMessageType.PLAIN)
            case 0x2: return self.consume_text_metadata(TextMessageType.COPYRIGHT)
            case 0x3: return self.consume_text_metadata(TextMessageType.TRACK_NAME)
            case 0x4: return self.consume_text_metadata(TextMessageType.INSTRUMENT_NAME)
            case 0x5: return self.consume_text_metadata(TextMessageType.LYRIC)
            case 0x6: return self.consume_text_metadata(TextMessageType.MARKER)
            case 0x7: return self.consume_text_metadata(TextMessageType.CUE_POINT)
            case 0x20: return ChannelPrefixMessage(self.consume_to_int(1), self.consume_to_int(1))
            case 0x2F: 
                self.validate_and_consume([0])
                return TrackCompleteMessage()
            case 0x51: return SetTempoMessage(SetTempoData(self.consume_to_int(1), self.consume_to_int(3)))
            case 0x54: return SmpteOffsetMessage(SmpteOffsetData(self.consume_to_int(1), self.consume(5)))
            case 0x58: return SetTimeSignatureMessage(SetTimeSignatureData(
                self.consume_to_int(1), 
                self.consume_to_int(1),
                self.consume_to_int(1),
                self.consume_to_int(1),
                self.consume_to_int(1),
            ))
            case 0x59: return SetKeySignatureMessage(SetKeySignatureData(self.consume_to_int(1), self.consume_to_int(1), self.consume_to_int(1)))
            case 0x7F: 
                length = self.consume_to_int(1)
                data_bytes = self.consume(length)
                return SetSeqInfoMessage(SetSeqInfoData(length, data_bytes))


    def consume_text_metadata(self, text_type: TextMessageType):
        length = self.consume_to_int(1)
        data_bytes = self.consume(length)
        data = TextData(length, data_bytes)

        return TextMessage(text_type, data)

    def validate_and_consume(self, expected_bytes):
        for expected in expected_bytes:
            actual = self.data[self.ptr]
            if actual != expected:
                raise Exception(f"Unexpected byte at position {self.ptr}. Expected {hex(expected)}, got {hex(actual)}.{self.context()}")
            
            self.advance()

    def consume(self, byte_count: int) -> 'list[int]':
        bytes = []
        for i in range(0, byte_count):
            bytes.append(self.data[self.ptr])
            self.advance()

        return bytes
    
    def consume_to_int(self, byte_count: int) -> int:
        return bytes_to_int(self.consume(byte_count))

    def advance(self):
        self.ptr = self.ptr + 1

    def peek(self, byte_count: int) -> 'list[int]':
        return self.data[self.ptr : self.ptr + byte_count]
    
    def context(self, byte_count: int = 4) -> str:
        pre = ' '.join(map(lambda i : hex(i), self.data[self.ptr - byte_count - 1 : self.ptr - 1]))
        post = ' '.join(map(lambda i : hex(i), self.data[self.ptr : self.ptr + byte_count]))
        this_byte = hex(self.data[self.ptr - 1])
        return f"\nCurrent pointer position ({self.ptr}): {pre} << {this_byte} >> {post}"
    
def hex_string_to_bytes(byte_string: str):
    return list(map(lambda s : int(s, 16), byte_string.split()))

def bytes_to_int(bytes):
    return int.from_bytes(bytes, byteorder='big', signed=False)