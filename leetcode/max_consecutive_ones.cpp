#include <algorithm>
#include <vector>

// number: 1004
// title: Max Consecutive Ones III
// url: https://leetcode.com/problems/max-consecutive-ones-iii/
// section: sliding window
// difficulty: medium
// tags: array, binary search, sliding window, prefix sum, leetcode 75

// constraints
// 1 <= nums.length <= 10^5
// nums[i] is either 0 or 1.
// 0 <= k <= nums.length
// k: how many 0s to flip

// complexity
// run-time: O(n)
// space: O(1)
int maxConsecutiveOnes(std::vector<int>& nums, int k)
{
    int left = 0;
    int ans = 0;
    int curr = 0;

    for (int right = 0; right != nums.size(); ++right) {
        // count 0s
        if (nums[right] == 0) {
            ++curr;
        }

        while (curr > k) {
            // remove 0s
            if (nums[left] == 0) {
                --curr;
            }

            // shrink window
            ++left;
        }

        ans = std::max(ans, right-left+1);
    }

    return ans;
}
