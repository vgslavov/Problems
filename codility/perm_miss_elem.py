# 100% both
def solution(A):
    n = len(A)+1
    sa = sum(A)
    sn = n*(n+1)/2
    return sn - sa

# http://codesays.com/2014/solution-to-perm-missing-elem-by-codility/ 
def solution(A):
    n = len(A)
    k = 0 
    for i in range(n):
        k = k ^ A[i] ^ (i+1)
    return k ^ (n+1)