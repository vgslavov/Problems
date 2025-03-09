#include <algorithm>
#include <limits>
#include <vector>

// number: 918
// section: Kadane's algo
// difficulty: medium
// tags: array, divide & conquer, dp, queue, monotonic queue

// constraints
// n == nums.length
// 1 <= n <= 3 * 10^4
// -3 * 10^4 <= nums[i] <= 3 * 10^4
// return the maximum possible sum of a *non-empty* subarray of nums

// solution: Kadane's algo + calc total/min sum
// complexity
// run-time: O(n)
// space: O(1)
int maxSubarraySumCircular(const std::vector<int>& nums)
{
    if (nums.empty()) {
        return 0;
    }

    int totalSum = 0;
    int currMaxSum = 0;
    int currMinSum = 0;
    int maxSum = std::numeric_limits<int>::min();
    int minSum = std::numeric_limits<int>::max();

    for (const auto& n : nums) {
        currMaxSum = std::max(n, currMaxSum+n);
        maxSum = std::max(maxSum, currMaxSum);

        currMinSum = std::min(n, currMinSum+n);
        minSum = std::min(minSum, currMinSum);

        totalSum += n;
    }

    // total_sum == min_sum when all n < 0
    return totalSum == minSum ? maxSum : std::max(maxSum, totalSum-minSum);
}

// TODO: add unit tests
