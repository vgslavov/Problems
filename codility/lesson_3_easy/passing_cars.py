# 100% both
def solution(A):
    ne = 0
    nw = 0
    np = 0
    
    for v in A:
        if v == 0:
            ne += 1
        elif v == 1:
            nw += 1
            np += ne
            if np > 1000000000:
                return -1
        # invalid input
        else:
            return -1
                
    return np

# 66%: 100% correctness, 40% performance
def solution(A):
    n = len(A)
    west = 0
    east = 0
    passed = 0
    
    for i in xrange(n):
        if A[i] == 0:
            east += 1
        else:
            west += 1
            if east:
                passed += east
    
    return passed
