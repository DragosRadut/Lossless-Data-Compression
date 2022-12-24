compressed_file = open('output.bin', 'rb')

# read number of unique characters to int
unique_chars = compressed_file.read(1)
unique_chars = int.from_bytes(unique_chars, "big")
	
print(unique_chars)

#for i in range(4) :
	#aux = compressed_file.read(1)
	#print(aux.decode("ascii"))
	
code = compressed_file.read()
print(type(code))
aux = int.from_bytes(code, "big")
print(bin(aux))
#print(str(code, "utf-8"))
