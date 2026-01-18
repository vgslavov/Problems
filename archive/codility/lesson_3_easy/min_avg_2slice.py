# %?
import sys
def solution(A):
    n = len(A)
    p = [0] * (n+1)
    min_start_val = sys.float_info.max
    min_val = sys.float_info.max
    min_idx = 0

    # compute prefix sum
    for i in xrange(1, n+1):
        p[i] = p[i-1] + A[i-1]

    for i in xrange(2, n+1):
        min_start_val = (p[i] - p[min_idx]) / float(i-min_idx)

        #lmin_val = min(min_start_val, A[i])
        if min_start_val < A[i]:
            lmin_val = min_start_val
        else:
            lmin_val = A[i]
            min_idx = i

        min_val = min(min_val, lmin_val)

   return min_idx
   
# 60%: 100% correctness, 20% performance: O(n^2) or O(n^3)
import sys
def solution(A):
    n = len(A)
    p = [0] * (n+1)
    min_val = sys.float_info.max
    min_idx = 0

    for i in xrange(1, n+1):
        p[i] = p[i-1] + A[i-1]
    
    # i ends 2 before j!
    for i in xrange(0, n-1):
        # j starts 2 after i!
        for j in xrange(i+2, n+1):
            # force float!
            lmin_val = (p[j] - p[i]) / float(j-i)
            if lmin_val < min_val:
                min_val = lmin_val
                min_idx = i
    return min_idx

# O% correctness
import sys
def solution(A):
    n = len(A)
    p = [0] * (n+1)
    min_idx = 0
    min_val = sys.float_info.max
    
    for i in xrange(1, n+1):
        p[i] = p[i-1] + A[i-1]
        
    for i in xrange(0, n+1):
        for j in xrange(i+2, n+1):
            lomin_val = (p[j] - p[i]) / (j-i)
            if lomin_val < min_val:
                min_val = lomin_val
                min_idx = i+1
                
    return min_idx
