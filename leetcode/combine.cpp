#include <vector>

// number: 77
// title: Combinations
// url: https://leetcode.com/problems/combinations/
// section: backtracking
// difficulty: medium
// tags: backtracking, top 150

// constraints
// 1 <= n <= 20
// 1 <= k <= n

// solution: LeetCode backtracking
// complexity
// run-time: O(n choose k)
// space: O(k)

std::vector<std::vector<int>> ans;

void backtrack(std::vector<int> curr, int i, int n, int k)
{
    // base
    if (curr.size() == k) {
        ans.push_back(curr);
        return;
    }

    for (int j = i; j != n+1; ++j) {
        curr.push_back(j);
        backtrack(curr, j+1, n, k);
        curr.pop_back();
    }
}

// solution: LeetCode backtracking
// complexity
// run-time: O(k*n / (n-k)!*k!)
// space: O(k)
std::vector<std::vector<int>> combine(int n, int k)
{
    backtrack(std::vector<int>{}, 1, n, k);
    return ans;
}