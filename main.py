from lsh import get_candidates
import pandas as pd


def main():
    ind_list = pd.read_csv("index.csv")
    distances = ["cosine", "jaccard", "hamming"]
    br = [(250, 20), (500, 10), (31, 160)]

    for d, dist in enumerate(distances):
        print("For " + dist.title() + " Signatures")
        sig_mat = pd.read_csv(dist + "_signatures.csv")
        candidates = get_candidates(sig_mat, br[d][0], br[d][1])
        indDF = pd.DataFrame(candidates)
        indDF.to_csv("pairs/" + dist + "_pairs.csv")
        tpc, tp, tc = 0, 0, 100
        print("Candidate pairs:")
        for i, j in candidates:
            tp = tp + 1
            if j % 5 == i % 5:
                tpc = tpc + 1
            print(ind_list.iloc[i - 1, 2], ind_list.iloc[j - 1, 2])
        print("Precision :", tpc / tp)
        print("Recall : ", tpc / tc, end="\n\n")


if __name__ == '__main__':
    main()
