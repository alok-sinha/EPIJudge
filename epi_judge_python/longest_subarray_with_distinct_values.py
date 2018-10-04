from test_framework import generic_test


def longest_subarray_with_distinct_entries(A):
    # TODO - you fill in here.

    maxW, start = 0, 0
    d = {}
    for i, c in enumerate(A):
        if c not in d:
            d[c]=i
        else:
            maxW = max(maxW, i-start)
            print(i, start)

            del d[c]
            if d.keys():
                start = min(d.keys())

            d[c]= i

    return max(maxW, len(A)-1-start)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "longest_subarray_with_distinct_values.py",
            'longest_subarray_with_distinct_values.tsv',
            longest_subarray_with_distinct_entries))
