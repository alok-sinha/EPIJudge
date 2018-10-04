from test_framework import generic_test


def find_first_missing_positive(A):
    # TODO - you fill in here.


    if not A:
        return 1

    n, i = len(A),0
    #print(n)

    while i < n:
        num = A[i]
        #print(num)
        if (num >= 0) and (A[i] != i) and (num < n) and  (A[num] != num):
            #print (i,num)
            A[num], A[i] = A[i], A[num]
        else:
            i += 1


    if n == 1:
        return 1 if A[0] != 1 else 2

    nxt = 1
    for i in range(1, n):
        if A[i] != i:
            return i
        nxt += 1

    return nxt


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("first_missing_positive_entry.py",
                                       'first_missing_positive_entry.tsv',
                                       find_first_missing_positive))
