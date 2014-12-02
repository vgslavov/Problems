# 100% on both
# O(N) time, O(1) space
# can also use 1 counter (and check for 0)
def solution(S):
    left = 0
    right = 0
    
    for v in S:
        if v == '(':
            left += 1
        elif v == ')':
            right += 1
            # check if left < right
            if left < right:
                return 0
            
    if left == right:
        return 1
        
    return 0

# 12%: 33% correctness, 0% performance
def solution(S):
    left = 0
    right = 0
    
    for v in S:
        if v == '(':
            left += 1
        elif v == ')':
            right += 1
            # ATTN: check if left < right
            
    if left == right:
        return 1
        
    return 0
