# Non-DeterministicFST
A quick'n dirty (*hacky*) Python implementation of NFST parsing, for educational purposes. NLTK does not offer FST support anymore for Python 3+, and extand FST implementations (that I am aware of) are non-trivial to install and use.

File nfstParser.py contains the FST parser.
Example FSTs with inputs are in simpleNFST.pt and Pinyin2HinduArabicNumeralNFST.py.

To run:
cat nfstParser.py simpleNFST.pt > fst.py
Python fst.py

