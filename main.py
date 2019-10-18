from lsh import Buckets
import pandas as pd

ind_list = pd.read_csv("index.csv")
distances = ["cosine", "jaccard", "hamming"]
br = [(250, 20), (500, 10), (31, 160)]
# for d in distances:
#     print("For "+d+" Signatures")
#     pairDF = pd.read_csv("pairs/" + d + "_pairs.csv");
#     pairs = pairDF.values;
#     tpc, tp=0,0
#     for p in pairs:
#         i,j=p[1],p[2]
#         print(ind_list.iloc[i-1,2],ind_list.iloc[j-1,2])
#         tp+=1
#         if i%5 == j%5:
#             tpc+=1
#     print("Precision :",tpc/tp)
#     print("\n")


for d in range(len(distances)):
    buc = Buckets(distances[d] + "_signatures.csv", br[d][0], br[d][1])
    B = buc.get_buckets()
    ind = []
    tc = 100
    tpc, tp = 0, 0
    for i in range(1, 101):
        for j in range(i + 1, 101):
            if B[i][j] > 0:
                tp = tp + 1
                ind.append([i, j])
                if j % 5 == i % 5:
                    tpc = tpc + 1
    print("For " + distances[d] + " Signatures")
    print("Precision :", tpc / tp)
    print("Recall : ", tpc / tc)
    indDF = pd.DataFrame(ind)
    indDF.to_csv("pairs/" + distances[d] + "_pairs.csv")
    for i, j in ind:
        print(ind_list.iloc[i - 1, 2], ind_list.iloc[j - 1, 2])
    print("\n\n")
