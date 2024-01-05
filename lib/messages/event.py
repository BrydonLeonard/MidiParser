from lib.messages.message import MidiMessage

class MidiEvent():
    def __init__(self, delta_time: int, message: MidiMessage):
        self.delta_time = delta_time
        self.message = message

    def str_with_pre_time(self, time):
        return f"[{str(self.delta_time + time).rjust(10, '0')}] {self.message.__repr__()}"