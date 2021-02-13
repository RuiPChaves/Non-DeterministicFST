## Non-DeterministicFST
A quick'n dirty (*hacky!*) Python implementation of FST parsing, for educational purposes. NLTK does not offer FST support anymore for Python 3+, and extant Python FST implementations (that I am aware of) are non-trivial to install and use. 

**nfstParser.py** contains the FST parser.

**simpleNFST.pt** and **Pinyin2HinduArabicNumeralFST.py** are example FSTs and their input.

### To run:
`cat nfstParser.py simpleNFST.pt > fst.py`

`python fst.py`
