# 100% both
def solution(A):
    n = len(A)
    count = [0] * (n+1)
    for v in A:
        # out of range
        if v > n:
            return 0
        # duplicate
        elif count[v]:
            return 0
        else:
            count[v] += 1
        
    return 1
