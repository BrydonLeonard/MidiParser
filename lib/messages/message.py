from enum import Enum
from lib.messages.data import NoteData, Data, ControlChangeData, ChannelPressureData, PitchWheelChangeData

class MidiMessageType(Enum):
    NOTE_ON = 1
    NOTE_OFF = 2
    KEY_AFTER_TOUCH = 3
    CONTROL_CHANGE = 4
    PROGRAM_CHANGE = 5
    CHANNEL_AFTER_TOUCH = 6
    PITCH_WHEEL_CHANGE = 7

class MidiMessage():
    def __init__(self, channel: int, message_type: MidiMessageType):
        self.message_type = message_type
        self.channel = channel
        self.data = None

    def __repr__(self) -> str:
        return f"[Channel {str(self.channel).rjust(2, ' ')}] {self.data}"


class NoteOnMessage(MidiMessage):
    def __init__(self, channel: int, note_data: NoteData):
        MidiMessage.__init__(self, channel, MidiMessageType.NOTE_ON)
        self.data = note_data

class NoteOffMessage(MidiMessage):
    def __init__(self, channel: int, note_data: NoteData):
        MidiMessage.__init__(self, channel, MidiMessageType.NOTE_OFF)
        self.data = note_data

class KeyAfterTouchMessage(MidiMessage):
    def __init__(self, channel: int, note_data: NoteData):    
        MidiMessage.__init__(self, channel, MidiMessageType.KEY_AFTER_TOUCH)
        self.data = note_data

class ControlChangeMessage(MidiMessage):
    def __init__(self, channel: int, control_change_data: ControlChangeData):
        MidiMessage.__init__(self, channel, MidiMessageType.CONTROL_CHANGE)
        self.data = control_change_data

class ProgramChangeMessage(MidiMessage):
    def __init__(self, channel: int, new_program: Data):
        MidiMessage.__init__(self, channel, MidiMessageType.PROGRAM_CHANGE)
        self.data = new_program

class ChannelPressureMessage(MidiMessage):
    def __init__(self, channel: int, new_channel: ChannelPressureData):
        MidiMessage.__init__(self, channel, MidiMessageType.CHANNEL_AFTER_TOUCH)
        self.data = new_channel

class PitchWheelChangeMessage(MidiMessage):
    def __init__(self, channel: int, pitch_wheel_change_data: PitchWheelChangeData):
        MidiMessage.__init__(self, channel, MidiMessageType.PITCH_WHEEL_CHANGE)
        self.data = pitch_wheel_change_data
        






    

