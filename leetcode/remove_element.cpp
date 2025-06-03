#include <vector>

// number: 27
// title: Remove Element
// url: https://leetcode.com/problems/remove-element/
// section: array/string
// difficulty: easy
// tags: array, two pointers, top 150

// constraints
// remove in-place
// 0 <= nums.length <= 100
// 0 <= nums[i] <= 50
// 0 <= val <= 100

// solution: sort
// complexity
// run-time: O(n*log n)
// space: O(1)
int removeElement(std::vector<int>& nums, int val)
{
    int matches = 0;

    for (auto & n : nums) {
        if (n == val) {
            n = std::numeric_limits<int>::max();
            ++matches;
        }
    }

    std::sort(nums.begin(), nums.end());

    return nums.size() - matches;
}

// TODO: add unit tests & solve linearly with two pointers