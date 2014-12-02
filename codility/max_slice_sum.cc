// 100%
#include <algorithm>
int solution(const vector<int> &A) {
    // in case one element only
    long long max_end = A[0];
    long long max_slice = A[0];
    
    // start from 2nd element!
    for (int i = 1; i < (int)A.size(); i++) {
        long long num = A[i];
        max_end = max(num, max_end + A[i]);
        max_slice = max(max_slice, max_end);
    }
    return max_slice;
}


// 53%
#include <algorithm>
int solution(const vector<int> &A) {
    int max_end = 0;
    int max_slice = 0;
    
    for (int i = 0; i < (int)A.size(); i++) {
        max_end = max(0, max_end + A[i]);
        max_slice = max(max_end, max_slice);
    }
    return max_slice;
}
