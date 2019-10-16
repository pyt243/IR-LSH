import pandas as pd
import numpy as np
import os
import glob

class Matrix:
    def __init__(self):
        self.path = r'corpus-20090418/'

    def retrieve_docs(self):
        direc = glob.glob(self.path + "*.txt")
        direc.sort()
        index=[]
        text=[]
        for i in range(len(direc)):
            ind = [i+1,direc[i]]
            index.append(ind)
            f = open(direc[i],"r",encoding="utf8", errors='ignore')
            s = ""
            for x in f:
                if x != '\n':
                    s=s+x.strip()
            text.append(s)
        ind_df = pd.DataFrame(index,columns=['index','document'])
        ind_df.to_csv(r'index.csv')
        return text

    def get_shingles(self,text):
        k = 5
        shingles = []
        for t in text:
            for i in range(len(t)-k+1):
                shingles.append(t[i:i+k])
        shingles.sort()        
        shingles = set(shingles)
        return shingles

    def create_matrix(self,shingles,text):
        mat=[]
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
        matdf.to_csv(r'shingles_matrix.csv')


if __name__ == "__main__":
    m = Matrix()
    d = m.retrieve_docs()
    print(d[8])
    print(len(d[8])-4)
    x = m.get_shingles(d)
    m.create_matrix(x,d)
