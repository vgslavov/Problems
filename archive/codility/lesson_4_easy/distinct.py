# 100% both
def solution(A):
    n = len(A)
    dist = 0
    
    if n == 0:
        return 0
    
    A.sort()
    dist = 1
    for i in xrange(1, n):
        if A[i] != A[i-1]:
            dist += 1
            
    return dist

# 66%: 55% correctness, 100% performance
# distinct values, not non-repeating values!
def solution(A):
    n = len(A)
    dist = 0

    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    A.sort()
    for i in xrange(n-1):
        if A[i] != A[i+1]:
            dist += 1
    
    if A[n-1] != A[n-2]:
        dist += 1
    
    return dist