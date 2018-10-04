from test_framework import generic_test


def calculate_largest_rectangle(heights):
    # TODO - you fill in here.
    n = len(heights)
    left, right = 0, n - 1

    maxSoFar = 0
    i,j = 0,0
    while left < right:
        area = min(heights[left], heights[right]) * (right - left)
        if area > maxSoFar:
            maxSoFar = area
            i,j = left, right

        if heights[left] > heights[right]:
            right -= 1
        else:
            left += 1

    print(i,j)
    return maxSoFar


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("largest_rectangle_under_skyline.py",
                                       'largest_rectangle_under_skyline.tsv',
                                       calculate_largest_rectangle))
