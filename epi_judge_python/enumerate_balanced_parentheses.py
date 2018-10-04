from test_framework import generic_test, test_utils


def generate_balanced_parentheses(num_pairs):
    # TODO - you fill in here.

    def addParan(s, left, right):
        if right < left:
            return

        if left == 0 and right == 0:
            ret.append(s)
            return

        if left:
            addParan(s + "(", left - 1, right)
        if right:
            addParan(s + ")", left, right - 1)

    s = ""
    ret = []
    addParan(s, num_pairs, num_pairs)
    return ret



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("enumerate_balanced_parentheses.py",
                                       'enumerate_balanced_parentheses.tsv',
                                       generate_balanced_parentheses,
                                       test_utils.unordered_compare))
