# O(n)
def prefix_sums(A):
    n = len(A)
    p = [0] * (n+1)
    for k in xrange(1, n+1):
        p[k] = p[k-1] + A[k-1]

    return p

# totals of m slices (x,y)
# 0 <= x <= y < n
# calculate separately: O(n * m)
# using prefix sum: O(n + m), p_(y+1) - p_x
