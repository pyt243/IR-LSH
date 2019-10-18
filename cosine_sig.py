import pandas as pd
import numpy as np
from numpy.linalg import norm


class Cosine_Sig:
    """
    Generates signatures of the input matrix based on cosine similarity
    """

    def __init__(self):
        self.sh_path = "shingles_matrix.csv"
        self.hash_num = 5000

    def get_rand_planes(self, ndim, odim):
        """
        Generates ndim number of random planes

        Args:
            ndim (int) : Required number of planes
            odim (int) : The number of dimensions in each plane
        Returns:
            list : Random planes generated
        """
        rand_proj = np.random.randn(ndim, odim)
        return rand_proj

    def get_signatures(self):
        """
        Generates signatures of the input matrix and stores it.
        """
        Mdf = pd.read_csv(self.sh_path)
        rand_proj = self.get_rand_planes(self.hash_num, len(Mdf["1"].values))
        col = len(Mdf.columns) - 2
        Sig = [[0 for i in range(col + 1)] for j in range(self.hash_num)]
        for i in range(1, col + 1):
            doc = Mdf[str(i)].values
            for j in range(self.hash_num):
                cos = np.dot(doc, rand_proj[j])
                if cos >= 0:
                    Sig[j][i] = 1
        SigDF = pd.DataFrame(Sig)
        SigDF.to_csv("cosine_signatures.csv")


if __name__ == "__main__":
    c = Cosine_Sig()
    c.get_signatures()
    Mdf = pd.read_csv("shingles_matrix.csv")
    Sdf = pd.read_csv("cosine_signatures.csv")
    a1 = Mdf["3"].values
    a2 = Sdf["3"].values
    b1 = Mdf["8"].values
    b2 = Sdf["8"].values
    c1 = np.dot(a1, b1) / (norm(a1) * norm(b1))
    cnt = 0
    for i in range(5000):
        if a2[i] == b2[i]:
            cnt = cnt + 1
    c2 = (cnt / 5000 - 0.5) * 2
    print(c1, c2)
