import os
import numpy as np
import pandas as pd

class Buckets:


    def __init__(self):
        self.cos_path="cosine_signatures.csv"

        
    def get_buckets(self):
        Sig_Mat=pd.read_csv(self.cos_path)
        col=len(Sig_Mat.columns)-1;
        Bucket=[[0 for x in range(col)] for y in range(col)]
        b=250
        r=20
        for i in range(0,b):
            for j in range(1,col):
                a=Sig_Mat.iloc[i*r:(i+1)*r,j+1]
                for k in range(j+1,col):
                    b=Sig_Mat.iloc[i*r:(i+1)*r,k+1]
                    if a.equals(b):
                        Bucket[j][k]+=1               
        return Bucket            





if __name__ == '__main__':
    t=Buckets()
    ind_list=pd.read_csv("index.csv")
    Bucket=t.get_buckets();
    for i in range(1,101):
        for j in range(i+1,101):
            if Bucket[i][j]>0:
      	        print(ind_list.iloc[i-1,2],ind_list.iloc[j-1,2])
   