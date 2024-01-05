
from Scanner import Scanner

def hex_string_to_bytes(byte_string: str):
    return list(map(lambda s : int(s, 16), byte_string.split()))

file = open("Bass_sample.mid", 'rb')
bytes = list(file.read())

scanner = Scanner(bytes)
midi_file = scanner.parse()

print(midi_file)