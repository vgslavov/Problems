#include <vector>

// number: 560
// title: Subarray Sum Equals K
// url: https://leetcode.com/problems/subarray-sum-equals-k/
// difficulty: medium
// tags: array, hash table, prefix sum

// constraints:
// 1 <= nums.length <= 2 * 10^4
// -1000 <= nums[i] <= 1000
// -107 <= k <= 10^7

// solution: prefix sum with brute force
// complexity:
// run-time: O(n^2), not TLE!
// space: O(n)
int subarraySum(const std::vector<int>& nums, int k)
{
    std::vector<int> prefix{0};
    int ans = 0;

    // build prefix sum
    for (int i = 1; i <= nums.size(); ++i) {
        prefix.push_back(prefix[i-1]+nums[i-1]);
    }

    for (int i = 0; i != nums.size(); ++i) {
        for (int j = i+1; j != prefix.size(); ++j) {
            if (prefix[j] - prefix[i] == k) {
                ++ans;
            }
        }
    }

    return ans;
}

// TODO: add unit tests