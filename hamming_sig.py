import pandas as pd
import numpy as np


class Hamming_Sig:
    """
    Generates signatures of a matrix based on hamming distance
    """

    def __init__(self):
        self.sh_path = "shingles_matrix.csv"
        self.hash_num = 5000

    def get_signatures(self):
        """
        Generates signatures of the input matrix and stores it
        """
        Mdf = pd.read_csv(self.sh_path)
        M = Mdf.values
        col = len(Mdf.columns) - 2
        Sig = []
        for i in range(self.hash_num):
            random_num = np.random.randint(0, len(M))
            row = M[random_num][1:]
            row[0] = 0
            Sig.append(row)
        SigDF = pd.DataFrame(Sig)
        SigDF.to_csv("hamming_signatures.csv")


if __name__ == "__main__":
    h = Hamming_Sig()
    h.get_signatures()
    Mdf = pd.read_csv("shingles_matrix.csv")
    Sdf = pd.read_csv("hamming_signatures.csv")
    a1 = Mdf["3"].values
    a2 = Sdf["3"].values
    b1 = Mdf["8"].values
    b2 = Sdf["8"].values
    c1, c2 = 0, 0
    for i in range(len(a1)):
        if a1[i] != b1[i]:
            c1 = c1 + 1
    for i in range(5000):
        if a2[i] != b2[i]:
            c2 = c2 + 1
    print(c1, c2 * 23722 / 5000)
