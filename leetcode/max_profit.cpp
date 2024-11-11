#include <limits>
#include <vector>

// number: 121
// section: array/string
// difficulty: easy
// tags: array, dynamic programming, top 150, citadel

// constraints
// 1 <= prices.length <= 10^5
// 0 <= prices[i] <= 10^4
// limit to 1 buy & 1 sell
// have to buy *before* you sell (can't short)


// solution: one pass to find biggest diff by finding cheapest price
// complexity
// run-time: O(n)
// space: O(1)
int maxProfit(std::vector<int>& prices) {
    int ans = std::numeric_limits<int>::min();
    int min_idx = 0;

    for (size_t i = 1; i != prices.size(); ++i) {
        int profit = prices[i] - prices[min_idx];
        ans = std::max(ans, profit);

        if (prices[i] < prices[min_idx]) {
            min_idx = i;
        }
    }

    if (ans < 0) {
        return 0;
    }

    return ans;
}

// TODO: add unit tests
