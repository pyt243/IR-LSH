import os
import numpy as np
import pandas as pd
from statistics import median


class Euclidean:
    """
    Generates signatures of input matrix based on Euclidean distance .
    """

    def __init__(self):
        self.sh_path = "shingles_matrix.csv"

    def get_dist(self, vec):
        """
        Computes L2 norm of a vector

        Args:
            vec (list) : Input vector representing a document
        Returns:
            int : L2 norm the input vector
        """
        return np.linalg.norm(vec)

    def get_signatures(self):
        """
        Generates signatures of the input matrix and stores it
        """
        SMat = pd.read_csv(self.sh_path)
        rand_proj = np.random.randn(5000, len(SMat["1"].values))
        col = len(SMat.columns) - 2
        Sig = [[0 for i in range(col + 1)] for j in range(5000)]
        for i in range(5000):
            l = []
            l.append(0)
            for j in range(1, col + 1):
                doc = SMat[str(j)].values
                dist = self.get_dist(doc - rand_proj[i])
                l.append(dist)
            med = median(l)
            for j in range(1, col + 1):
                if l[j] <= med:
                    Sig[i][j] = 1
        SigDF = pd.DataFrame(Sig)
        SigDF.to_csv("euclidean_signatures.csv")


if __name__ == "__main__":
    obj = Euclidean()

    obj.get_signatures()
