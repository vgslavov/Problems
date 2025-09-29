#include <queue>
#include <vector>

// tags: heap

// solution: min heap
// complexity:
// run-time: O(n*log k)
// space: O(k)
int findKthLargest(const std::vector<int> nums, int k)
{
    if (nums.empty()) {
        return 0;
    }

    // min heap: kth largest will be on top of min heap
    std::priority_queue<int, std::vector<int>, std::greater<int>> heap;

    for (const auto& n : nums) {
        heap.push(n);

        if (heap.size() > k) {
            heap.pop();
        }
    }

    return heap.top();
}

// solution: AlgoMonster max heap
// complexity:
// run-time: O(n+k*log n), heapify + pop
// space: O(n)
int findKthLargest2(const std::vector<int> nums, int k)
{
    if (nums.empty()) {
        return 0;
    }

    // max heap: std::vector is optional w/o greater/less
    // O(n)
    std::priority_queue<int> heap(nums.begin(), nums.end());

    // O(k*log n)
    for (size_t i = 0; i != k-1; ++i) {
        heap.pop();
    }

    return heap.top();
}