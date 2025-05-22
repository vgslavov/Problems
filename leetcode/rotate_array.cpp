#include <algorithm>
#include <deque>
#include <vector>

// number: 189
// title: Rotate Array
// url: https://leetcode.com/problems/rotate-array/
// section: array/string
// difficulty: medium
// tags: array, math, two pointers, top 150

// constraints
// 1 <= nums.length <= 10^5
// -2^31 <= nums[i] <= 2^31 - 1
// 0 <= k <= 10^5

// solution: deque manual
// complexity
// run-time: O(n)
// space: O(n)
void rotate(std::vector<int>& nums, int k)
{
    std::deque<int> queue(nums.begin(), nums.end());

    while (k > 0) {
        queue.push_front(queue.back());
        queue.pop_back();
        --k;
    }

    nums.clear();
    std::copy(queue.begin(), queue.end(), std::back_inserter(nums));
}

// TODO: add unit tests & solve in-place w/ O(1)
