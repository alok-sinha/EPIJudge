from test_framework import generic_test, test_utils


def generate_power_set(S):
    # TODO - you fill in here.


    result = []
    n = len(S)
    s = []

    def AddElement(i):
        if i == n:
            result.append(list(s))
            return

        AddElement(i+1)

        s.append(S[i])
        AddElement(i+1)
        s.pop()

    AddElement(0)

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("power_set.py", 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))
