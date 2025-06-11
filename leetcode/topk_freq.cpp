#include <queue>
#include <unordered_map>
#include <vector>

// number: 347
// title: Top K Frequent Elements
// url: https://leetcode.com/problems/top-k-frequent-elements/
// section: meta
// difficulty: medium
// tags: array, hash table, divide & conquer, sorting, heap,
// bucket sort, counting, quickselect, meta

// constraints
// 1 <= nums.length <= 10^5
// -10^4 <= nums[i] <= 10^4
// k is in the range [1, the number of unique elements in the array].
// It is guaranteed that the answer is unique.

// solution: map + min priority queue
// complexity
// run-time: O(n + u*log k) where u is unique
// space: O(n)

using pi = std::pair<int, int>;

std::vector<int> topKFrequent(const std::vector<int>& nums, int k)
{
    std::unordered_map<int, int> counts;

    for (const auto& n : nums) {
        ++counts[n];
    }

    std::priority_queue<pi, std::vector<pi>, std::greater<pi>> minHeap;

    for (const auto& pair : counts) {
        minHeap.push(std::make_pair(pair.second,pair.first));

        if (minHeap.size() > k) {
            minHeap.pop();
        }
    }

    std::vector<int> ans;
    
    while (!minHeap.empty()) {
        ans.push_back(minHeap.top().second);
        minHeap.pop();
    }

    return ans;
}

// TODO: add unit tests