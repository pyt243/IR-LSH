import pandas as pd
import numpy as np
import random
from numpy.linalg import norm


class Jaccard_Sig:
    """
    Generates signatures of the input matrix based on  Jaccard similarity.
    """

    hash_num = 5000
    max_shingles = 10 ** 5
    MOD = 1000003

    def __init__(self):
        self.sh_path = "shingles_matrix.csv"

    def get_rand_coeffs(self, k):
        """
        Generates random number which act of coefficients for random hash functions.

        Args:
            k (int) : Number of hash functions.
        Returns:
            list : Random coefficients of hash functions
        """
        rand_list = []

        while k > 0:
            random_num = random.randint(0, self.max_shingles)

            while random_num in rand_list:
                random_num = random.randint(0, self.max_shingles)

            k = k - 1
            rand_list.append(random_num)

        return rand_list

    def get_signatures(self):
        """
        Generates signatures of the input matrix and stores it
        """
        Mdf = pd.read_csv(self.sh_path)
        A = self.get_rand_coeffs(self.hash_num)
        B = self.get_rand_coeffs(self.hash_num)

        col = len(Mdf.columns) - 2
        Sig = [[self.MOD for i in range(col + 1)] for j in range(self.hash_num)]

        for i in range(1, col + 1):
            doc = Mdf[str(i)].values
            print(doc)
            for j in range(0, self.hash_num):
                minhash = self.MOD + 1
                shingle_id = 1
                for k in doc:
                    if k == 1:
                        hash = (A[j] * shingle_id + B[j]) % self.MOD
                        if hash < minhash:
                            minhash = hash
                    shingle_id = shingle_id + 1
                Sig[j][i] = minhash

        SigDF = pd.DataFrame(Sig)
        SigDF.to_csv("jaccard_signatures.csv")


if __name__ == "__main__":
    # c = Jaccard_Sig()
    # c.get_signatures()
    Mdf = pd.read_csv("shingles_matrix.csv")
    Jdf = pd.read_csv("jaccard_signatures.csv")
    a1 = Mdf["2"].values
    a2 = Jdf["2"].values
    b1 = Mdf["8"].values
    b2 = Jdf["8"].values
    c1 = np.dot(a1, b1) / (norm(a1) * norm(b1))
    intersection = 0
    union = 5000
    for i in range(union):
        if a2[i] == b2[i]:
            intersection = intersection + 1

    c2 = intersection / union
    print(c1, c2)
