#include <vector>
#include <unordered_map>

// number: 219
// title: Contains Duplicate II
// url: https://leetcode.com/problems/contains-duplicate-ii/
// section: hashmap
// difficulty: easy
// tags: array, hash table, sliding window, top 150

// description
// return true if there are two distinct indices i and j in the array such that
// nums[i] == nums[j] and abs(i - j) <= k

// constraints
// 1 <= nums.length <= 10^5
// -10^9 <= nums[i] <= 10^9
// 0 <= k <= 10^5

// solution: hashmap
// complexity
// run-time: O(n)
// space: O(k)
bool containsNearbyDuplicate(const std::vector<int>& nums, int k)
{
    std::unordered_map<int, std::vector<int>> num2index;

    for (size_t i = 0; i != nums.size(); ++i) {
        num2index[nums[i]].push_back(i);
    }

    for (const auto& item : num2index) {
        for (size_t i = 1; i != item.second.size(); ++i) {
            if (abs(item.second[i]-item.second[i-1]) <= k) {
                return true;
            }
        }
    }

    return false;
}

// TODO: solve using sliding window & add unit tests