# 100% both: O(N + M)
def solution(N, A):
    counters = [0] * N
    cur_max = 0
    max_op = 0
    
    # M
    for v in A:
        if v <= N:
            # apply lazy max_counter
            if max_op > counters[v-1]:
                counters[v-1] = max_op + 1
            else:
                counters[v-1] += 1

            # update max
            if cur_max < counters[v-1]:
                cur_max = counters[v-1]
        if v == (N+1):
            # record lazy max_counter
            max_op = cur_max
    
    # N
    # apply the rest of the lazy max_counter
    for i in xrange(N):
        if counters[i] < max_op:
            counters[i] = max_op
            
    return counters

# 11%: 25% correctness
def solution(N, A):
    counters = [0] * N
    cur_max = 0
    max_op = 0
    
    for v in A:
        if v <= N:
            if max_op > counters[v-1]:
                counters[v-1] = max_op + 1
            else:
                counters[v-1] += 1
            if cur_max < counters[v-1]:
                cur_max = counters[v-1]
        if v == (N+1):
            # lazy max_counter
            max_op = cur_max
    
    # damn iterator!
    # (works on example)
    for i in counters:
        if counters[i] < max_op:
            counters[i] = max_op
            
    return counters

# 66%: 100% correctness, 40% performance: O(N*M)
def solution(N, A):
    counters = [0] * N
    lmax = 0
    
    # M
    for v in A:
        if v <= N:
            counters[v-1] += 1
            if lmax < counters[v-1]:
                lmax = counters[v-1]
        if v == (N + 1):
            # N
            for i in xrange(N):
                counters[i] = lmax

    return counters

# 77%: 100% correctness, 60% performance
def solution(N, A):
    counters = [0] * N
    lmax = 0
    
    for v in A:
        if v <= N:
            counters[v-1] += 1
            if lmax < counters[v-1]:
                lmax = counters[v-1]
        if v == (N + 1):
            # too slow!
            counters = [lmax] * N
    
    return counters

# 66%: 100% correctness, 40% performance: O(N*M)
def solution(N, A):
    counters = [0] * N
    
    # M
    for v in A:
        if v <= N:
            counters[v-1] += 1
        if v == (N + 1):
            # N
            m = max(counters)
            counters = [m] * N
    
    return counters

