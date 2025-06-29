#include <vector>

// number: 78
// title: Subsets
// url: https://leetcode.com/problems/subsets/
// section: backtracking
// difficulty: medium
// tags: backtracking

// constraints
// 0 <= nums.length <= 10
// -10 <= nums[i] <= 10

std::vector<std::vector<int>> ans;

void backtrack(const std::vector<int>& nums, std::vector<int> curr, int i)
{
    if (i > nums.size()) {
        return;
    }

    ans.push_back(curr);

    for (size_t j = i; j != nums.size(); ++j) {
        curr.push_back(nums[j]);
        backtrack(nums, curr, j+1);
        curr.pop_back();
    }
}

// solution: LeetCode backtracking
// complexity
// run-time: O(n*2^n)
// space: O(n)
std::vector<std::vector<int>> subsets(const std::vector<int>& nums)
{
    backtrack(nums, std::vector<int>{}, 0);

    return ans;
}