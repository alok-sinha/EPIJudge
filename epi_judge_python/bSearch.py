


def rightMostOccurance(A, num):
    left, right = 0, len(A)-1

    found = -1
    while left <= right:
        mid = (left + right)//2

        if A[mid] == num:
            left = mid + 1
            found = mid
        elif A[mid] < num:
            left = mid + 1
        else:
            right = mid - 1

    return found if found != -1 else left



A = [1,2,4,5,6,6,6,9,9]
print(rightMostOccurance(A, 9))
