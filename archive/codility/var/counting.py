def counting(A, m):
    n = len(A)
    count = [0] * (m+1)
    for i in xrange(n):
        count[A[i]] += 1
    return count
