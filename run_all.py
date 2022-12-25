import os
import sys
method = str(sys.argv[1])

if method == 'huff' :
	for i in range(1, 10) :
		os.system('python ./huffman/huff_compress.py test' + str(i))
		os.system('python ./huffman/huff_decode.py ./out/test' + str(i))
else:
	if method == 'lz77' :
		for i in range(1, 10) :
			os.system('python ./lz77/lz77_compress.py test' + str(i))
			os.system('python ./lz77/lz77_decode.py ./out/test' + str(i))
if method == 'other' :
	os.system('python ./huffman/huff_compress.py new_test')
	os.system('python ./huffman/huff_decode.py ./out/new_test')
	os.system('python ./lz77/lz77_compress.py new_test')
	os.system('python ./lz77/lz77_decode.py ./out/new_test')
