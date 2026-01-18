# 100% on both
# time: O(N logN)
def solution(A):
    n = len(A)
    A.sort()

    # A[n-1] is never evaluated!
    # last index evaluated is n-2
    # (stops after i == n-1 is over)
    for i in xrange(1, n-1):
        found = 0
        if A[i-1] + A[i] > A[i+1]:
            found += 1
        if A[i] + A[i+1] > A[i-1]:
            found += 1
        if A[i+1] + A[i-1] > A[i]:
            found += 1
        if found == 3:
            return 1
            
    return 0

# 43% total: 30% correctness, 66% performance
def solution(A):
    n = len(A)
    A.sort()

    # wrong stop index
    for i in xrange(1, n-2):
        found = 0
        if A[i-1] + A[i] > A[i+1]:
            found += 1
        if A[i] + A[i+1] > A[i-1]:
            found += 1
        if A[i+1] + A[i-1] > A[i]:
            found += 1
        # ATTN: find at least one (p,q,r) triple
        if found == 3:
            return 1
            
    return 0
