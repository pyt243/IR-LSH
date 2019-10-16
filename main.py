from lsh import Buckets
import pandas as pd

ind_list=pd.read_csv("index.csv")
distances = ['cosine']
for d in distances:
    buc = Buckets(d+"_signatures.csv")
    B = buc.get_buckets()
    ind=[]
    tc = 500
    tpc,tp=0,0
    for i in range(1,101):
        for j in range(i+1,101):
            if B[i][j]>0:
                tp=tp+1
                ind.append((i,j))
                if j%5 == i%5:
                    tpc=tpc+1
    print("For "+d+" Signatures")
    print("Precision :",tpc/tp)
    print("Recall : ",tpc/tc)
    for i,j in ind:
      	print(ind_list.iloc[i-1,2],ind_list.iloc[j-1,2])
    print("\n\n")
