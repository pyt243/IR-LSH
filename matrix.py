import pandas as pd
import numpy as np
import os
import glob


class Matrix:
    """
    Extract text from corpus and prepares the document index and shingles matrix (0-1 matrix)
    """

    def __init__(self):
        self.path = r"corpus-20090418/"

    def retrieve_docs(self):
        """
        Function to retrieve docs, extract text from them and index the documents.

        Returns:
            list : Documents/text extracted from files
        """
        direc = glob.glob(self.path + "*.txt")
        direc.sort()
        index = []
        text = []
        for i in range(len(direc)):
            ind = [i + 1, direc[i]]
            index.append(ind)
            f = open(direc[i], "r", encoding="utf8", errors="ignore")
            s = ""
            for x in f:
                if x != "\n":
                    s = s + x.strip()
            text.append(s)
        ind_df = pd.DataFrame(index, columns=["index", "document"])
        ind_df.to_csv(r"index.csv")
        return text

    def get_shingles(self, text):
        """
        Generates uniques shingles from the extracted text.

        Args:
            text (list) : A list of strings representing documents
        Returns:
            set : A set of possible shingles present in the corpus
        """
        k = 5
        shingles = []
        for t in text:
            for i in range(len(t) - k + 1):
                shingles.append(t[i : i + k])
        shingles.sort()
        shingles = set(shingles)
        return shingles

    def create_matrix(self, shingles, text):
        """
        Prepares the 0-1 matrix from the extracted text and shingles and stores it.

        Args:
            shingles (set) : set of shingles
            text (list) : List of strings repesenting documents

        """
        mat = []
        for s in shingles:
            row = []
            row.append(s)
            for t in text:
                if s in t:
                    row.append(1)
                else:
                    row.append(0)
            mat.append(row)
        matdf = pd.DataFrame(mat)
        matdf.to_csv(r"shingles_matrix.csv")


if __name__ == "__main__":
    m = Matrix()
    d = m.retrieve_docs()
    print(d[8])
    print(len(d[8]) - 4)
    x = m.get_shingles(d)
    m.create_matrix(x, d)
