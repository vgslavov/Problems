#include <map>
#include <vector>

// number: 1
// title: Two Sum
// url: https://leetcode.com/problems/two-sum/
// section: hashmap
// difficulty: easy
// tags: array, hash table, top 150

// constraints
// 2 <= nums.length <= 10^4
// -10^9 <= nums[i] <= 10^9
// -10^9 <= target <= 10^9
// Only one valid answer exists.

// solution: brute-force
// complexity
// run-time: O(n^2), slow
// space: O(1)
std::vector<int> twoSum1(const std::vector<int>& nums, int target)
{
    for (int i = 0; i != nums.size(); ++i) {
        // start at 1!
        for (int j = 1; j != nums.size(); ++j) {
            if (i != j && nums[i] + nums[j] == target) {
                return std::vector<int>{i, j};
            }
        }
    }

    return std::vector<int>{-1,-1};
}

// solution: map
// complexity
// run-time: O(n)
// space: O(n)
std::vector<int> twoSum2(const std::vector<int>& nums, int target)
{
    std::map<int, int> num2index;

    for (int i = 0; i != nums.size(); ++i) {
        int sub = target - nums[i];

        auto it = num2index.find(sub);
        if (it != num2index.end()) {
            return std::vector<int>{i, it->second};
        }

        num2index[nums[i]] = i;
    }

    return std::vector<int>{-1,-1};
}

// TODO: add unit tests
