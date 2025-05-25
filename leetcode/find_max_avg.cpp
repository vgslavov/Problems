#include <algorithm>
#include <limits>
#include <vector>

// number: 643
// title: Maximum Average Subarray I
// url: https://leetcode.com/problems/maximum-average-subarray-i/
// section: sliding window
// difficulty: easy
// tags: array, sliding window, leetcode 75

// constraints
// n == nums.length
// 1 <= k <= n <= 10^5
// -10^4 <= nums[i] <= 10^4

// solution: sliding window
// complexity
// run-time: O(n)
// space: O(1)
double findMaxAverage(std::vector<int>& nums, int k)
{
    double ans = std::numeric_limits<double>::min();
    double sum = 0;

    for (int i = 0; i < k; ++i) {
        sum += nums[i];
    }

    ans = sum / k;

    for (int i = k; i < nums.size(); ++i) {
        // add current & remove first!
        sum += nums[i] - nums[i-k];
        ans = std::max(ans, sum/k);
    }

    return ans;
}

// TODO: write unit tests
