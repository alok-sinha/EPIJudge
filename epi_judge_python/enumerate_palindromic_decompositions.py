from test_framework import generic_test


def palindrome_decompositions(input):
    # TODO - you fill in here.

    result = []
    current = []


    def checkPalindrom(s,start,end):
        while start < end:
            if s[start] != s[end]:
                return False
            start, end = start+1, end-1

        return True

    def breakIntoPalindrom(s):
        if not s:
            result.append(list(current))

        for i in range(0, len(s)):
            p = checkPalindrom(s, 0, i)
            if p:
                current.append(s[0:i+1])
                breakIntoPalindrom(s[i+1:])
                current.pop()


    breakIntoPalindrom(input)
    return result


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "enumerate_palindromic_decompositions.py",
            'enumerate_palindromic_decompositions.tsv',
            palindrome_decompositions, comp))
