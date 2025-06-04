#include <vector>

// number: 1480
// title: Running Sum of 1d Array
// url: https://leetcode.com/problems/running-sum-of-1d-array/
// section: array/string
// difficulty: easy
// tags: array, prefix sum

// constraints
// 1 <= nums.length <= 1000
// -10^6 <= nums[i] <= 10^6

// solution: prefix sum
// complexity
// run-time: O(n)
// space: O(n)
std::vector<int> runningSum(const std::vector<int>& nums) {
    if (nums.empty()) {
        return std::vector<int>();
    }

    std::vector<int> runSum{nums.front()};

    for (size_t i = 1; i != nums.size(); ++i) {
        runSum.push_back(runSum.back() + nums[i]);
    }

    return runSum;
}