class Data():
    def __init__(self, data: int):
        self.data = data

class NoteData():
    def __init__(self, note: int, velocity: int):
        self.note = note
        self.velocity = velocity

    def __repr__(self):
        return f"Play {note_index_to_name(self.note)} with velocity {self.velocity}"
    
class ProgramChangeData(Data):
    def __init__(self, new_program: int):
        self.data = new_program

    def __repr__(self):
        return f"Switch to program {self.data}"

class ControlChangeData(Data):
    def __init__(self, controller_number: int, new_controller_value: int):
        self.controller_number = controller_number
        self.new_controller_value = new_controller_value

    def __repr__(self) -> str:
        return f"Adjust controller {self.controller_number} to value {self.new_controller_value}"

class ChannelPressureData(Data):
    def __init__(self, pressure: int):
        self.pressure = pressure

    def __repr__(self) -> str:
        return f"Apply pressure of {self.pressure}"

class PitchWheelChangeData(Data):
    def __init__(self, data: int):
        if (data & 0x3fff != data): # 3FFF is 14 1s, the max size for pitch wheel data
            raise Exception(f"Pitch wheel data '{data}' is invalid")
        
    def __repr__(self) -> str:
        pitch_change = (self.data - 0x2000) / (0x3fff - 0x2000) * 2 # 0x2000 is halfway and full deflection is two semitons
        if (pitch_change > 0):
            pitch_direction = "upwards"
        else:
            pitch_direction = "downwards"
        return f"Adjust the pitch {abs(pitch_change)} semitones {pitch_direction}"

note_names = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    
def note_index_to_name(index: int):
    octave = index // 12 
    note = note_names[index % 12]

    return f"{note}{octave}"