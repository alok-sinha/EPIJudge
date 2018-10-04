from test_framework import generic_test


def majority_search(stream):
    # TODO - you fill in here.
    #Alok
    count = 1
    majorityElem = ''

    for el in stream:
        if el == majorityElem:
            count += 1
        else:
            count -= 1
            if count == 0:
                majorityElem = el
                count = 1

    return majorityElem


def majority_search_wrapper(stream):
    return majority_search(iter(stream))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("majority_element.py",
                                       'majority_element.tsv',
                                       majority_search_wrapper))
