from test_framework import generic_test


def find_maximum_subarray(A):
    # TODO - you fill in here.
    if not len(A):
        return 0

    maxSum = A[0] if A[0] > 0 else 0
    maxSumSofar = maxSum
    for i in range(1,len(A)):
        num = A[i]
        if num + maxSum > maxSum:
            maxSum = num + maxSum
            if maxSumSofar < maxSum:
                maxSumSofar = maxSum
            print(maxSumSofar, maxSum, num)
        else:
            maxSum = 0
            print("0")


    return maxSumSofar


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("max_sum_subarray.py",
                                       'max_sum_subarray.tsv',
                                       find_maximum_subarray))
