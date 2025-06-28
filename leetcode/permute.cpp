#include <vector>

// number: 46
// title: Permutations
// url: https://leetcode.com/problems/permutations/
// section: backtracking
// difficulty: medium
// tags: array, backtracking, top 150, meta

// constraints
// 1 <= nums.length <= 6
// -10 <= nums[i] <= 10
// All the integers of nums are unique.

std::vector<std::vector<int>> ans;

// pass curr by value
void backtrack(const std::vector<int>& nums, std::vector<int> curr)
{
    // base case:
    if (curr.size() == nums.size()) {
        ans.push_back(curr);
        return;
    }

    for (const auto& n : nums) {
        // not found
        if (std::find(curr.begin(), curr.end(), n) == curr.end()) {
            curr.push_back(n);
            backtrack(nums, curr);
            curr.pop_back();
        }
    }
}

// solution: LeetCode backtracking
// complexity
// run-time: O(n*n!)?
// space: O(n*n!)?
std::vector<std::vector<int>> permute(const std::vector<int>& nums) {
    backtrack(nums, std::vector<int>{});

    return ans;
}