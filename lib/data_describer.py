class DataDescriber():
    def __init__(self, bytes: 'list[int]', explanation: str, known_byte_length: int = None):
        self.bytes = list(bytes)
        self.explanation = explanation
        if known_byte_length is None:
            self.known_byte_length = len(self.bytes)
        else:
            self.known_byte_length = known_byte_length

    def from_int(bytes: int, explanation: str, known_byte_length: int = None):
        # Figure out how many orders of magnitude we're working with in base 256
        byte_count = 1
        working_val = bytes
        while (working_val > 256):
            working_val = working_val // 256
            byte_count = byte_count + 1

        return DataDescriber(bytes.to_bytes(byte_count, 'big'), explanation, known_byte_length)

    # Bytes are a string of the form 'ff ff ff ff ...'
    def from_str(bytes: str, explanation: str, known_byte_length: int = None):
        return DataDescriber(hex_string_to_bytes(bytes), explanation, known_byte_length)
    
    def __repr__(self):
        padded = self.bytes

        byte_str = " ".join(map(lambda b : str(hex(b).replace("0x", "").rjust(2, '0')), padded))

        return f"{byte_str.rjust(40, ' ')} |> {self.explanation}"
    
    def padded_bytes(self) -> 'list[int]':
        padded = self.bytes
        
        while (len(padded) < self.known_byte_length):
            padded.insert(0, 0)

        return padded


        

# Just copy/pasted from Scanner for now
def hex_string_to_bytes(byte_string: str):
    return list(map(lambda s : int(s, 16), byte_string.split()))