# ---Huffman Encoding---
import sys
input_path = str(sys.argv[1])
output_path = './out/' + input_path + '.out1'

# input to string
with open('./in/' + input_path + '.in') as f:
	input_data = f.read()

# create dictionary of input letters
frecv = dict()
for char in input_data:
	frecv[char] = frecv.get(char, 0) + 1


# dictionary to list with reversed key value for optimisation
# using key = frecvency / value = character 
# list sort method will sort by key (if equal, sort by value)
ch_list = []
chars = frecv.keys()
for char in chars:
	ch_list.append((frecv[char], char))
ch_list.sort()

# creating huffman tree, represented as a nested single-noded list
while len(ch_list) > 1:
	first = tuple(ch_list[0:2])
	last = ch_list[2:]
	first_frecv = first[0][0] + first[1][0]
	ch_list = last + [(first_frecv, first)]
	ch_list.sort(key = lambda x: x[0])

# trimming frecvency	
def trim (tree) :
	node = tree[1]
	if type(node) == type("") : return node
	else : return (trim(node[0]), trim(node[1]))

# generating codes
code = {}
def createCodes(node, pattern='') :
	if type(node) == type("") :
		code[node] = pattern
	else :
		createCodes(node[0], pattern+"0")
		createCodes(node[1], pattern+"1")

	
out = trim(ch_list[0])	
createCodes(out)

output = ""
for ch in input_data :
	output += code[ch]

# file header
out_file = open(output_path, "wb")

unique_chars = len(code)
out_file.write(unique_chars.to_bytes(1, 'big'))
for key, value in code.items():
	output_string = key + value + "~"
	out_file.write(output_string.encode('latin-1'))
out_file.write(int(output, 2).to_bytes((len(output) + 7) // 8, "big"))

out_file.close()

