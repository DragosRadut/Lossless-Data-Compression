# Lossless-Data-Compression
Implementation provides an demonstational approach of in use compression methods.
` Comparative analysis and detailed explanation : `
[Algorithm-Analysis.pdf](./Algorithm-Analysis.pdf)

## Running
``` 
make run-huff (Huffman's method)
make run-lz77 (LZ77 method)
```
Both run rules use **run_all.py**. Encoded binary files are stored in **out** directory. Decoded files are stored in **decompressed** directory. Test are found in **in** directory.

### Other test
**in** directory contains **new_test** designed to be replaced for testing individual input:
```
make run-other (both methods)
```




