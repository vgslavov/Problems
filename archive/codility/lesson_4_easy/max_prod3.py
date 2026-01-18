# 100% both
def solution(A):
    n = len(A)
    A.sort()
    # if many negative numbers, multiplying neg. gives positive
    return max(A[0] * A[1] * A[n-1], A[n-3] * A[n-2] * A[n-1])
    # or using negative indices
    #return max(A0] * A[1] * A[-1], A[-3] * A[-2] * A[-1])