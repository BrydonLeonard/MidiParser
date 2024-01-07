
from Scanner import Scanner
import functools

def flatten(list: list):
    flat_list = []
    for xs in list:
        for x in xs:
            flat_list.append(x)
    return flat_list

file = open("Bass_sample.mid", 'rb')
bytes = list(file.read())

scanner = Scanner(bytes)
json_repr, descriptions = scanner.parse()

bytes_from_descriptions = flatten(list(map(lambda description : description.padded_bytes(), descriptions)))

zipped = list(zip(bytes_from_descriptions, bytes))

bytes_match = functools.reduce(lambda previous, pair : (pair[0] == pair[1]) and previous, zipped)

if not bytes_match:
    raise Exception("Bytes don't match")


print('\n'.join(map(lambda d : d.__repr__(), descriptions)))
