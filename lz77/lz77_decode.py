# ---LZ77 Encoding---
# ---Dragos Radut---
import sys
input_path = str(sys.argv[1])
input_path += '.out2'

output_path = './decompressed' + input_path[5:]
def read_from_file() :
	# 3 byte parsing
	offset_bits = 11
	length_bits = 5
	offset_length_bytes = 2
	
	with open(input_path, 'rb') as f :
		compressed = bytearray(f.read())

	while len(compressed) > 0 :
		# restore 11 bites = offset + 5 bites = length
		offset_length_value = 0
		for aux in range(offset_length_bytes) :
			offset_length_value = (offset_length_value * 256) + int(compressed.pop(0))
		offset = offset_length_value >> length_bits
		length = offset_length_value & ((2 ** length_bits) - 1)
		
		if offset > 0 :
			char_out = None
		else :
			char_out = str(chr(compressed.pop(0)))
		
		input_data.append((offset, length, char_out))
	
input_data = []
read_from_file()

# execute
x=0
out = ""
while x < len(input_data):
	(offset, length, char) = input_data[x]
	x += 1
	if length == 0 :
		if char is not None :
			out += char
	else :
		if char is not None :
			out += char
			length -= 1
			offset = 1
		start_id = len(out) - offset
		for i in range(length) :
			out += out[start_id + i]


with open(output_path, "w") as f :
	f.write(out)

