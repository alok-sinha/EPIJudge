from test_framework import generic_test

from collections import defaultdict

def next_permutation(perm):
    # TODO - you fill in here.

    count = defaultdict(int)
    found = False
    n = len(perm)
    count[perm[n-1]] = 1
    maxNum = perm[n-1]
    i = None
    for i in range(n-2, -1, -1):
        count[perm[i]] += 1
        maxNum = perm[i] if perm[i] > maxNum else maxNum
        if perm[i] < perm[i+1]:
            found = True
            break

    nextPerm = perm[:i] if i else []

    if found:
        x = perm[i]
        for j in range(x+1,maxNum+1):
            if j in count:
                nextPerm.append(j)
                count[j] -= 1
                break

        for j in range(0,maxNum+1):
            if j in count:
                while count[j]:
                    nextPerm.append(j)
                    count[j] -= 1

    return nextPerm


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "next_permutation.py", 'next_permutation.tsv', next_permutation))
