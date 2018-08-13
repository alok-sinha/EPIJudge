from test_framework import generic_test


def remove_duplicates(L):
    # TODO - you fill in here.

    print("List:: ",type(L))

    if not L:
        return 0

    read, write = 1,1
    num = L[0]
    while read < len(L):
        if L[read] != num:
            L[write] = L[read]
            num = L[write]
            write = write +1

        read += 1

    return write


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "remove_duplicates_from_sorted_list.py",
            'remove_duplicates_from_sorted_list.tsv', remove_duplicates))
