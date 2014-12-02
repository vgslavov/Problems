// 100%
int solution(const vector<int> &A) {
    long long sumleft = 0;
    long long sumright = 0;
    long long sum = 0;
    
    if (A.empty())
        return -1;
    
    for (int i = 0; i < (int)A.size(); i++) {
        sum += (long long) A[i];
    }
        
    for (int i = 0; i < (int)A.size(); i++) {
        sumright = sum - sumleft - (long long)A[i];
        if (sumleft == sumright) return i;
        sumleft += (long long) A[i];
    }
    return -1;
}

// 56% (old)
int solution_old(const vector<int> &A) {
    long sumleft = 0;
    long sumright = 0;
    
    if (A.empty())
        return -1;
    else if (A.size() == 1)
        return -1;
    
    for (int i = 2; i < (int)A.size(); i++) {
        sumright += A[i];
    }
        
    sumleft = A[0];
    
    for (int i = 1; i < (int)(A.size() - 1); i++) {
        if (sumleft == sumright)
            return i;
        
        sumleft += A[i];
        sumright -= A[i+1];
    }
    return -1;
}
