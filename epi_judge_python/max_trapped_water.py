from test_framework import generic_test


def get_max_trapped_water(heights):
    # TODO - you fill in here.

    n = len(heights)
    left, right = 0, n-1

    maxSoFar = 0
    while left < right:
        area = min(heights[left],heights[right])*(right-left)
        if area > maxSoFar:
            maxSoFar = area

        if heights[left] > heights[right]:
            right -= 1
        else:
            left += 1

    return maxSoFar


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("max_trapped_water.py",
                                       "max_trapped_water.tsv",
                                       get_max_trapped_water))
