// 100%

#include <cstdlib>

int solution(vector<int> &A) {
    long sumleft = 0;
    long sumright = 0;
    long localmin;
    long ans;
    
    // start from 2nd element
    for (int i = 1; i < (int)A.size(); i++) {
        sumright += A[i];
    }
    
    sumleft = A[0];
    ans = abs(sumright - sumleft);
    
    for (int i = 1; i < (int)(A.size() - 1); i++) {
        sumleft += A[i];
        sumright -= A[i];
        localmin = abs(sumleft - sumright);
        if (localmin < ans) {
            ans = localmin;
        }
    }
    
    return ans;
}
