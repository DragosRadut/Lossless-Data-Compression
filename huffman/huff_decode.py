# ---Huffman decoding---
import sys
input_path = str(sys.argv[1])
input_path += '.out1'

output_path = './decompressed' + input_path[5:]

compressed_file = open(input_path, 'rb')

# read number of unique characters to int
unique_chars = compressed_file.read(1)
unique_chars = int.from_bytes(unique_chars, "big")

# read char = code dictionary
chars_found = 1
codes_dictionary = {}
last_char = compressed_file.read(1).decode("latin-1")

while chars_found <= unique_chars :
	code = ""
	char_input = compressed_file.read(1).decode("latin-1")
	while char_input != '~' :
		code += char_input
		char_input = compressed_file.read(1).decode("latin-1")
	codes_dictionary[last_char] = code
	chars_found += 1
	if chars_found <= unique_chars :
		last_char = compressed_file.read(1).decode("latin-1")

# read encoded string
encoded = compressed_file.read()
aux = int.from_bytes(encoded, "big")
encoded = bin(aux)

# decode
output = ""
i = 2
while i < len(encoded) :
	leaf = ""
	while leaf not in codes_dictionary.values() and i < len(encoded) :
		leaf += encoded[i]
		i += 1
	for key, value in codes_dictionary.items() :
		if value == leaf :
			output += key
			break;

out_file = open(output_path, "w")
out_file.write(output)
out_file.close()

