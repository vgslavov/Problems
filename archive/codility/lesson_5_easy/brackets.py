# 100% on both
# O(N) time and space
def solution(S):
    stack = []
    matched = {}
    matched[')'] = '('
    matched['}'] = '{'
    matched[']'] = '['
    
    for v in S:
        if v == '(' or v == '{' or v == '[':
            stack.append(v)
        else:
            # check if empty!
            if stack:
                top = stack.pop()
                if matched[v] != top:
                    return 0
            else:
                return 0
                
    if stack:
        return 0
        
    return 1

# 37% total: 33% correctness, 40% performance
def solution(S):
    stack = []
    matched = {}
    matched[')'] = '('
    matched['}'] = '{'
    matched[']'] = '['
    
    for v in S:
        if v == '(' or v == '[' or v == '{':
            stack.append(v)
        else:
            # ATTN: check if empty first!
            top = stack.pop()
            if matched[v] != top:
                return 0
                
    if stack:
        return 0
        
    return 1
