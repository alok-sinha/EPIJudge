from test_framework import generic_test


def longest_matching_parentheses(s):
    # TODO - you fill in here.

    print(s)

    stack = []
    longest = 0
    current = 0
    # ()())
    # ))()())
    #  (()()) ) ()()()()
    # )((())(((((
    for i,c in enumerate(s):
        if c == "(":
            stack.append(i)
        else: #")"
            if stack:
                x = stack.pop()
                current += i-x + 1
                longest = max(longest, current)
            else:
                #Spurious )
                current = 0




    return longest


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "longest_substring_with_matching_parentheses.py",
            'longest_substring_with_matching_parentheses.tsv',
            longest_matching_parentheses))
