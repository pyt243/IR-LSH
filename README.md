# Plagiarism Detector using LSH

This application is capable of extracting pairs similar documents
from a set of documents present in a corpus. Documents
containing similar texts are marked as a plagiarized pair.
Locality sensitive hashing is used to find similar pairs and various
distance measures such as Jaccard distance, Cosine distance and
Hamming distance are used in the process. For each distance
measure, a set of predicted plagiarized pairs are returned.

## Features
* Returns pairs of plagiarised or **similar** documents, which are answers to a question in our corpus.
* Three different measures (Jaccard distance, Cosine distance, Hamming distance) can be used to find similar documents.
* The algorithm shows the **precision** and **number of correct documents returned** for each distance measure.
* The signature matrix needs to be generated only once for each distance measure.
* Fully documented code.

## How to run
1. Clone this repo / click "Download as Zip" and extract the files.
2. Ensure Python 3.7 is installed, and in your system `PATH`.
3. Install pipenv using `pip install -U pipenv`.
4. In the project folder, run `pipenv install` to install all python dependencies.
5. Generate the shingle-document matrix by running: `pipenv run python matrix.py`. Matrix will be stored in **shingles_matrix.csv**.
6. To create the signature matrix:
	1. Jaccard distance: `pipenv run python jaccard_sig.py`.
		Signature matrix stores in **jaccard_signatures.csv**.
	2. Cosine distance: `pipenv run python cosine_sig.py`.
		Signature matrix stores in **cosine_signatures.csv**.
	3. Hamming distance: `pipenv run python hamming_sig.py`.
		Signature matrix stores in **hamming_signatures.csv**.
7. To run the LSH algorithm: `pipenv run python main.py`.
	