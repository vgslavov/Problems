#include <functional>
#include <iostream>
#include <queue>
#include <vector>

// number: 703
// similar: 215
// title: Kth Largest Element in a Stream
// url: https://leetcode.com/problems/kth-largest-element-in-a-stream/
// section:
// difficulty: easy
// tags: tree, design, bst, heap, binary tree, data stream

// constraints
// 1 <= k <= 10^4
// 0 <= nums.length <= 10^4
// -10^4 <= nums[i] <= 10^4
// -10^4 <= val <= 10^4
// At most 10^4 calls will be made to add.
// It is guaranteed that there will be at least k elements in the array when you
// search for the kth element.

// solution: min heap
// complexity
// run-time: O(log k) to add(), O(log n) to construct
// space: O(k)
class KthLargest {
public:
    KthLargest(int k, const std::vector<int>& nums)
    : d_k(k)
    {
        // don't init, have to go through all nums!
        for (const auto& n : nums) {
            add(n);
        }
    }

    int add(int val) {
        d_minHeap.push(val);

        // pop *after* adding!
        if (d_minHeap.size() > d_k) {
            d_minHeap.pop();
        }

        // top of min heap is kth largest
        return d_minHeap.top();
    }

private:
    int d_k;
    std::priority_queue<int, std::vector<int>, std::greater<int>> d_minHeap;
};

// Your KthLargest object will be instantiated and called as such:
KthLargest* obj = new KthLargest(k, nums);
int param_1 = obj->add(val);
