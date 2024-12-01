#include <algorithm>
#include <queue>
#include <vector>

// number: 215
// section: heap
// difficulty: medium
// tags: array, divide & conquer, sorting, heap, prio queue, quickselect, top 150,
// leetcode 75

// constraints
// 1 <= k <= nums.length <= 10^5
// -10^4 <= nums[i] <= 10^4

// solution: sort in-place
// complexity
// run-time: O(n*log n)
// space: O(1)
int findKthLargest(std::vector<int>& nums, int k)
{
    std::sort(nums.begin(), nums.end());

    return nums[nums.size()-k];
}

// solution: min heap
// complexity
// run-time: O(n*log k)
// space: O(k)
int findKthLargest2(const std::vector<int>& nums, int k)
{
    if (nums.empty()) {
        return 0;
    } else if (k == 1) {
        // O(n)
        return *std::max_element(nums.begin(), nums.end());
    }

    std::priority_queue<int, std::vector<int>, std::greater<int>> minHeap;

    for (const auto& n : nums) {
        minHeap.push(n);

        if (minHeap.size() > k) {
            minHeap.pop();
        }
    }

    return minHeap.top();
}

// TODO: add unit tests
