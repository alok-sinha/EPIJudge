from test_framework import generic_test, test_utils

from collections import defaultdict
def find_anagrams(dictionary):
    # TODO - you fill in here.
    # Alok
    anagrams = defaultdict(list)

    for word in dictionary:
        anagrams[tuple(sorted(word))].append(word)


    return [e for e in anagrams.values() if len(e) > 1]



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "anagrams.py",
            "anagrams.tsv",
            find_anagrams,
            comparator=test_utils.unordered_compare))
