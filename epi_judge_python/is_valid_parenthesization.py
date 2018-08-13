from test_framework import generic_test


def is_well_formed(s):
    # TODO - you fill in here.
    stack = []
    leftParan = ['(', '{', '[']
    opposite = {'(': ')', '{': '}', '[': ']'}

    for c in s:
        if c in leftParan:
            stack.append(c)
        else:
            if len(stack) > 0:
                c1 = stack.pop()
                if opposite[c1] != c:
                    return False
            else:
                return False

    return len(stack) == 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_valid_parenthesization.py",
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
