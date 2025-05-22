#include <algorithm>
#include <map>
#include <vector>

// number: 198
// title: House Robber
// url: https://leetcode.com/problems/house-robber/
// section: 1D DP
// difficulty: medium
// tags: array, dp, top 150

// constraints
// 1 <= nums.length <= 100
// 0 <= nums[i] <= 400

int dp(const std::vector<int>& nums, int i, std::map<int, int>& memo)
{
    // base case
    if (i == 0) {
        return nums[0];
    } else if (i == 1) {
        return std::max(nums[0], nums[1]);
    }

    // check cache
    auto it = memo.find(i);
    if (it != memo.end()) {
        return it->second;
    }

    // recurrence relation
    memo[i] = std::max(dp(nums, i-1, memo), dp(nums, i-2, memo)+nums[i]);

    return memo[i];
}

// solution: recursive top-down 1D DP using dict
// complexity
// run-time: O(n)
// space: O(n)
int rob(const std::vector<int>& nums)
{
    std::map<int, int> memo;
    return dp(nums, nums.size()-1, memo);
}

// solution: iterative bottom-up 1D DP
// complexity
// run-time: O(n)
// space: O(n)
int rob2(const std::vector<int>& nums)
{
    // init
    std::vector<int> dp(nums.size());

    // base cases
    if (nums.size() == 1) {
        return nums[0];
    }

    dp[0] = nums[0];
    dp[1] = std::max(nums[0], nums[1]);

    // recurrence relation
    for (size_t i = 2; i != nums.size(); ++i) {
        dp[i] = std::max(dp[i-1], dp[i-2]+nums[i]);
    }

    return dp[nums.size()-1];
}
