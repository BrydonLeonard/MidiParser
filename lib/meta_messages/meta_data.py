class TextData():
    def __init__(self, length: int, text_bytes: 'list[int]'):
        self.length = length
        self.text_bytes = text_bytes

class ChannelPrefixData():
    def __init__(self, length: int, channel: int):
        self.length = length
        self.channel = channel
        if self.length != 1:
            raise Exception(f"A length of {length} is invalid for channel prefix")

class SetSeqNumberData():
    def __init__(self, length: int, sequence_number: int):
        self.length = length
        self.sequence_number = sequence_number

micros_per_minute = 60000000
class SetTempoData():
    def __init__(self, length: int, micros_per_crotchet: int):
        self.length = length
        self.micros_per_crotchet = micros_per_crotchet

        if self.length != 3:
            raise Exception(f"A length of {length} is invalid for tempo data")
        
    def __repr__(self):
        return f"Set tempo to {micros_per_minute // self.micros_per_crotchet} bpm"
        
class SmpteOffsetData():
    def __init__(self, length: int, offset: int):
        self.length = length
        self.offset = offset

        if self.length != 5:
            raise Exception(f"A length of {length} is invalid for SMPTE offset")
        
    def __repr__(self):
        return f"This track's SMPTE offset is {self.offset}"
        
class SetTimeSignatureData():
    # I've honestly got no idea with this last arugment. I don't know how the ratio of a 32nd note to a quarter note would ever change.
    def __init__(self, length: int, numerator: int, denominator_exp: int, midi_ticks_per_metronome_click: int, demisemiquaver_per_crotchet: int):
        self.length = length
        self.numerator = numerator
        self.denominator = denominator_exp
        self.midi_ticks_per_metronome_click = midi_ticks_per_metronome_click
        self.demisemiquaver_per_crotchet = demisemiquaver_per_crotchet

        if self.length != 4:
            raise Exception(f"A length of {length} is invalid for time signature data")
        
    def __repr__(self):
        return f"Set time signature to {self.numerator}/{2**self.denominator}. Metronome will tick every {self.midi_ticks_per_metronome_click // 24} beat(s). There are {self.demisemiquaver_per_crotchet} demisemiquavers per crotchet"

class SetKeySignatureData():
    def __init__(self, length: int, sharps_flats: int, major_minor: bool):
        self.length = length
        self.sharps_flats = sharps_flats
        self.major_minor = major_minor

        if self.length != 2:
            raise Exception(f"A length of {length} is invalid for key signature data")

class SetSeqInfoData():
    def __init__(self, length: int, data: 'list[int]'):
        self.length = length
        self.data = data
        