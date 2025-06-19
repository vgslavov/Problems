#include <algorithm>
#include <vector>

// number: 283
// title: Move Zeroes
// url: https://leetcode.com/problems/move-zeroes/
// section: meta
// difficulty: easy
// tags: array, two pointers, meta

// constraints
// 1 <= nums.length <= 10^4
// -2^31 <= nums[i] <= 2^31 - 1
// in-place

// solution: sliding window
// complexity
// run-time: O(n)
// space: O(1)
void moveZeroes(std::vector<int>& nums) {
    int left = 0;

    for (size_t right = 0; right != nums.size(); ++right) {
        // find next non-zero
        if (nums[right] == 0) {
            continue;
        }

        // keep swapping
        if (nums[left] == 0) {
            std::swap(nums[left], nums[right]);
        } 

        ++left;
    }
}

// TODO: add unit tests