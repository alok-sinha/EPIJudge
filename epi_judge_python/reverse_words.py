import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a string encoded as bytearray.
def reverse_words(s):
    # TODO - you fill in here.

    def reverse(s, fr, to):
        left, right = fr, to
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right-1

    n = len(s)
    i = 0
    space, index = False, None

    while i < n:
        if not space:
            if chr(s[i]) != ' ':
                index = i
                space = True
        else:
            if chr(s[i]) == ' ':
                reverse(s, index, i-1)
                space = False

        i += 1
    if space:
        reverse(s, index, n-1)

    reverse(s,0, n-1)
    return


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = bytearray()
    s_copy.extend(map(ord, s))

    executor.run(functools.partial(reverse_words, s_copy))

    return s_copy.decode("utf-8")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_words.py", 'reverse_words.tsv',
                                       reverse_words_wrapper))
