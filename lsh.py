import os
import numpy as np
import pandas as pd


class Buckets:
    """
    Performs Loaclity Sensitive Hashing on generated Signatures.
    """

    def __init__(self, path, b, r):
        self.sig_path = path
        self.b = b
        self.r = r

    def get_buckets(self):
        """
        Hashes columns based on bands

        Returns:
            list : Matrix which specifies the candidate pairs
        """
        Sig_Mat = pd.read_csv(self.sig_path)
        col = len(Sig_Mat.columns) - 1
        Bucket = [[0 for x in range(col)] for y in range(col)]
        b = self.b
        r = self.r
        # for i in range(0,b):
        #     for j in range(1,col):
        #         a=Sig_Mat.iloc[i*r:(i+1)*r,j+1]
        #         for k in range(j+1,col):
        #             b=Sig_Mat.iloc[i*r:(i+1)*r,k+1]
        #             if a.equals(b):
        #                 Bucket[j][k]+=1
        for i in range(0, b):
            dict = {}
            for j in range(1, col):
                a = Sig_Mat.iloc[i * r : (i + 1) * r, j + 1]
                num = 0
                for k in a:
                    num = num * 10 + k
                if num in dict.keys():
                    dict[num].append(j)
                else:
                    dict[num] = [j]
            for k, v in dict.items():
                for x in range(0, len(v)):
                    for y in range(x + 1, len(v)):
                        Bucket[v[x]][v[y]] += 1
        return Bucket


if __name__ == "__main__":
    t = Buckets()
    ind_list = pd.read_csv("index.csv")
    Bucket = t.get_buckets()
    for i in range(1, 101):
        for j in range(i + 1, 101):
            if Bucket[i][j] > 0:
                print(ind_list.iloc[i - 1, 2], ind_list.iloc[j - 1, 2])
