import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

from collections import defaultdict
def decompose_into_dictionary_words(domain, dictionary):
    # TODO - you fill in here.

    cache = defaultdict(list)

    for i, c in enumerate(domain):

        if domain[:i+1] in dictionary:
            cache[i] = [domain[:i + 1]]

        x = []
        for offset in cache.keys():
            if domain[offset+1:i+1] in dictionary:
                x.append(domain[offset+1:i+1])
                cache[offset].append(domain[offset+1:i+1])
        if x:
            cache[i] = x

    print(cache)
    if len(domain)-1 in cache:
        print("yes", cache[len(domain)-1])
        return cache[0]
    else:
        print("no")
        return []


@enable_executor_hook
def decompose_into_dictionary_words_wrapper(executor, domain, dictionary,
                                            decomposable):
    result = executor.run(
        functools.partial(decompose_into_dictionary_words, domain, dictionary))

    if not decomposable:
        if result:
            raise TestFailure('domain is not decomposable')
        return

    if any(s not in dictionary for s in result):
        raise TestFailure('Result uses words not in dictionary')

    if ''.join(result) != domain:
        raise TestFailure('Result is not composed into domain')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "is_string_decomposable_into_words.py",
            'is_string_decomposable_into_words.tsv',
            decompose_into_dictionary_words_wrapper))
