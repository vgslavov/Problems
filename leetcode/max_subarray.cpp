#include <algorithm>
#include <limits>
#include <vector>

// number: 53
// title: Maximum Subarray
// url: https://leetcode.com/problems/maximum-subarray/
// section: Kadane's algo
// difficulty: medium
// tags: array, divide & conquer, dp, grind 75

// constraints
// 1 <= nums.length <= 10^5
// -10^4 <= nums[i] <= 10^4

// complexity
// run-time: O(n)
// space: O(1)
int maxSubArray(const std::vector<int>& nums) {
    int maxSum = std::numeric_limits<int>::min();
    int currSum = 0;

    for (const auto& n : nums) {
        currSum = std::max(currSum+n, n);
        maxSum = std::max(maxSum, currSum);
    }

    return maxSum;
}

// TODO: add unit tests
