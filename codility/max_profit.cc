// 100%
#include <algorithm>
#include <climits>
int solution(const vector<int> &A) {
    // set to max!
    long long min_price = LLONG_MAX;
    long long max_profit = 0;
    
    for (int i = 0; i < (int)A.size(); i++) {
        max_profit = max(max_profit, (long long)A[i] - min_price);
        min_price = min(min_price, (long long)A[i]);
    }
    return max_profit;
}