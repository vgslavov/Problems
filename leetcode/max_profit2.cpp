#include <vector>

// number: 122
// title: Best Time to Buy and Sell Stock II
// url: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
// section: array/string
// difficulty: medium
// tags: array, dp, greedy, top 150

// constraints
// 1 <= prices.length <= 3 * 10^4
// 0 <= prices[i] <= 10^4
// multiple buys & sells
// but hold at most one share of stock at a time

// solution: Leetcode greedy
// complexity
// run-time: O(n)
// space: O(1)
int maxProfit(const std::vector<int>& prices) {
    int profit = 0;
    for (size_t i = 1; i != prices.size(); ++i) {
        if (prices[i] > prices[i-1]) {
            profit += prices[i]-prices[i-1];
        }
    }

    return profit;
}

// TODO: solve using DP & add unit tests
