# 100% both
from collections import defaultdict
def solution(X, A):
    n = len(A)
    pos = defaultdict(int)
    for i in xrange(n):
        pos[A[i]] += 1
        if len(pos) == X:
            return i
            
    return -1
