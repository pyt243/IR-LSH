import pandas as pd
from collections import defaultdict
from itertools import combinations


def get_candidates(sig_mat: pd.DataFrame, b, r):
    """
    Performs Loaclity Sensitive Hashing on generated Signatures.
    Hashes columns based on bands

    Args:
        sig_mat (str) : Signature matrix generated using the LSH family
        b (int) : Number of bands
        r (int) : Number of rows per band

    Returns:
        set : The set of candidate pairs
    """
    num_cols = len(sig_mat.columns) - 1
    candidates = set()
    for i in range(0, b):
        bucket = defaultdict(list)
        for j in range(1, num_cols):
            a = sig_mat.iloc[i * r : (i + 1) * r, j + 1]
            col = ''.join(map(str, a))
            bucket[col].append(j)
        for values in bucket.values():
            candidates.update(combinations(values, 2))
    return candidates


if __name__ == "__main__":
    ind_list = pd.read_csv("index.csv")
    sig_mat = pd.read_csv('cosine_signatures.csv')
    candidates = get_candidates(sig_mat, 250, 20)
    for pair in candidates:
        print(ind_list.iloc[pair[0] - 1, 2], ind_list.iloc[pair[1] - 1, 2])
