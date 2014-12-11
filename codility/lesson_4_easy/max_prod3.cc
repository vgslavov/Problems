// 100%
#include <algorithm>
int solution(vector<int> &A) {
    int len = A.size();
    
    sort(A.begin(), A.end());
    
    // covers cases with negative numbers and 0s
    // the product of 1st 2 neg. numbers will be positive
    return max(A.front() * A[1] * A.back(), A[len-3] * A[len-2] * A.back());
}

// 0% (passed example only)
// fails:
// [-1, -1, 1, 7] returns -7 instead of 7
// [-1, -1, 0, 1, 7] returns 0 instead of 7
#include <algorithm>
int solution(vector<int> &A) {
    // write your code in C++98
    long int prq;
    int n = 3;
    sort(A.begin(), A.end());
    
    prq = A.back();
    for (int i = A.size()-2; i > 0 && n > 0; i--) {
        prq *= A[i];
        --n;
    }
    return prq;
}
