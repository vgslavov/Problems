#include <algorithm>
#include <vector>

// number: 55
// section: array / string
// difficulty: medium
// tags: array, greedy, dp, top 150

// constraints
// 1 <= nums.length <= 10^4
// 0 <= nums[i] <= 10^5

bool canJumpI(const std::vector<int>& nums, int i)
{
    if (i == nums.size()-1) {
        return true;
    }

    int farthest = std::min(i+nums[i], static_cast<int>(nums.size())-1);

    for (int j = i+1; j != farthest+1; ++j) {
        if (canJumpI(nums, j)) {
            return true;
        }
    }
    return false;
}

// non-solution: LeetCode backtracking
// complexity:
// run-time: O(2^n)
// space: O(n)
bool canJump(const std::vector<int>& nums)
{
    return canJumpI(nums, 0);
}

bool canJumpI2(const std::vector<int>& nums, int i, std::vector<int>& memo)
{
    // check cache
    if (memo[i] != -1) {
        return memo[i] == 1;
    }

    // can't jump farther than end of array
    int farthest = std::min(i+nums[i], static_cast<int>(nums.size())-1);

    // try all b/w next & farthest
    for (int j = i+1; j != farthest+1; ++j) {
        if (canJumpI2(nums, j, memo)) {
            memo[i] = 1;
            return true;
        }
    }

    memo[i] = 0;
    return false;
}

// solution: LeetCode top-down 1D recursive DP w/ memoization
// complexity:
// run-time: O(n^2)
// space: O(n)
bool canJump2(const std::vector<int>& nums)
 {
    // n-sized vector initialized to -1
    std::vector<int> memo(nums.size(), -1);
    // last index is always reachable
    memo.back() = 1;
    return canJumpI2(nums, 0, memo);
}

// solution: LeetCode bottom-up 1D iterative DP w/ memoization
// complexity:
// run-time: O(n^2)
// space: O(n)
bool canJump3(const std::vector<int>& nums) {
    std::vector<int> memo(nums.size(), -1);
    // last index is always reachable
    memo.back() = 1;

    // go right to left
    for (int i = nums.size(); i != 0;) {
        --i;
        int farthest = std::min(i+nums[i], static_cast<int>(nums.size())-1);

        for (int j = i+1; j != farthest+1; ++j) {
            // can reach j from i
            if (memo[j] == 1) {
                memo[i] = 1;
                // optimization: no need to check farther
                break;
            }
        }
    }

    // check if we can reach from the first index
    return memo[0] == 1;
}

// TODO: add unit tests