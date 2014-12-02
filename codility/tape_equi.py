# 100% both
def solution(A):
    left = A[0]
    right = sum(A[1:])
    min = abs(left-right)
    
    for i in range(1, len(A)-1):
        left += A[i]
        right -= A[i]
        diff = abs(left-right)
        if diff < min:
            min = diff
            
    return min

# 83% correctness, 100% performance
# fails for: 2 elements, small elements
import sys

def solution(A):
    left = 0
    right = sum(A)
    min = sys.maxint
        
    for i in A:
        left += i
        right -= i
        diff = abs(left-right)
        if diff < min:
            min = diff
            
    return min