#include <vector>

// number: 136
// title: Single Number
// url: https://leetcode.com/problems/single-number/
// section: bit manipulation
// difficulty: easy
// tags: array, bit manipulation, top 150, leetcode 75

// constraints
// 1 <= nums.length <= 3 * 10^4
// -3 * 10^4 <= nums[i] <= 3 * 10^4
// Each element in the array appears twice except for one element which appears
// only once.

// solution: xor 1 bitmask
// complexity
// run-time: O(n)
// space: O(1)
int singleNumber(const std::vector<int>& nums) {
    int mask = 0;

    // x ^ x = 0
    // 0 ^ y = y
    // x ^ x ^ y = y
    for (const auto& n : nums) {
        mask ^= n;
    }

    return mask;
}

// TODO: solve with toggling bits & unit test