# ---LZ77 Encoding---
# ---Dragos Radut---
import sys
input_path = str(sys.argv[1])
output_path = './out/' + input_path + '.out2'

# parsing on 3 bytes
def write_to_file (output) :
	# define mapping on bits
	offset_bits = 11
	length_bits = 5
	offset_length_bytes = 2
	
	bytes_output = bytearray()
	for value in output : 
		[(offset, length, char)] = value
		offset_length_value = (offset << length_bits) + length
		for count in range(offset_length_bytes) :
			bytes_output.append((offset_length_value >> (8 * (offset_length_bytes - 1 - count))) & (0b11111111))
		if char is not None :
			if offset == 0 :
				bytes_output.append(ord(char))
		else :
			bytes_output.append(0)
	
	out_file = open(output_path, "wb")
	out_file.write(bytes_output)
	out_file.close()

def search_pattern_length(window, string, limit) -> int :
	if window == "" or string == "" :
		return 0
	if limit > 31 : return 0
	
	# recursive search of length
	if window[0] == string[0] :
		return 1 + search_pattern_length(window[1:] + string[0], string[1:], limit + 1)
	return 0

def search(back, input_str) -> (int, int) :
	# offset can't be stored on 11 bits => adjust window
	if max_offset < len(back) : 
		window = back[-max_offset:]
	else : window = back
	
	if input_str == "" :
		return (0, 0)
	
	length = 1
	offset = 0
	
	recursion_limit = 0
	
	# not in dictionary so far
	if input_str[0] not in window : 
		found_length = search_pattern_length(input_str[0], input_str[1:], 0)
		return (min((length + found_length), max_length), offset)
	
	length = 0
	#print(input_data[0], " -> ", window)
	for i in range(1, (len(window) + 1)) :
		char = window[-i]
		if char == input_str[0] :
			found_offset = i
			recursion_limit = 0
			found_length = search_pattern_length(window[-i:], input_str, 0)
			if found_length > length :
				length = found_length
				offset = found_offset
				
	# length can't be stored on 5 bits => cut to max length
	return (min(length, max_length), offset)
	
	
# input to string
with open('./in/' + input_path + '.in') as f:
	input_data = f.read()

max_offset = 2047 # 11 bits
max_length = 31 # 5 bits

output = []
back = ""
while input_data != "" :
	length, offset = search(back, input_data)
	output.append([(offset, length, input_data[0])])
	back += input_data[:length]
	input_data = input_data[length:]


write_to_file(output)

