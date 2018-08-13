from test_framework import generic_test

#A[i] represents max step from this position, can we reach at end

def can_reach_end(A):
    # TODO - you fill in here.
    #print(A)
    if len(A) == 1:
        return True

    jumps = A[0]
    for jump in range(1,jumps+1):
       #print(jump)
       if can_reach_end(A[jump:]) == True:
           return True
    return False



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "advance_by_offsets.py", "advance_by_offsets.tsv", can_reach_end))
