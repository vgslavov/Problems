# 100% on both
# O(N) time, O(1) space
def solution(A):
    n = len(A)
    leader = -1
    size = 0
    
    for k in xrange(n):
        if size == 0:
            value = k
            size += 1
        else:
            if A[k] == A[value]:
                size += 1
            else:
                size -= 1
    
    if size == 0:
        return -1
    else:
        candidate = value
    
    count = 0    
    for k in xrange(n):
        if A[k] == A[candidate]:
            count += 1
    
    if count > n // 2:
        return candidate
    else:
        return -1
