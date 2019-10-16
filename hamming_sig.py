import pandas as pd
import numpy as np

class Hamming_Sig:

    def __init__(self):
        self.sh_path = "shingles_matrix.csv"
        self.hash_num = 5000

    def get_signatures(self):
        Mdf = pd.read_csv(self.sh_path)
        M = Mdf.values
        col = len(Mdf.columns)-2
        Sig = []
        for i in range(self.hash_num):
            random_num = np.random.randint(0,len(M))
            row = M[random_num][1:]
            Sig.append(row)
        SigDF = pd.DataFrame(Sig)
        SigDF.to_csv("hamming_signatures.csv")

if __name__ == "__main__":
        # h = Hamming_Sig()
        # h.get_signatures()
        Mdf = pd.read_csv("shingles_matrix.csv")
        Sdf = pd.read_csv("hamming_signatures.csv");
        a1 = Mdf['1'].values
        a2 = Sdf['1'].values
        b1 = Mdf['6'].values
        b2 = Sdf['6'].values
        c1,c2=0,0
        for i in range(len(a1)):
            if a1[i] != b1[i]:
                c1=c1+1
        for i in range(5000):
            if a2[i] != b2[i]:
                c2=c2+1
        print(c1,c2*23722/5000)
