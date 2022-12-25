run-huff:
	python run_all.py huff

run-lz77:
	python run_all.py lz77

run-best:
	python run_all.py lz77
	
run-other:
	python run_all.py other
clean:
	rm -rf ./out/.*
