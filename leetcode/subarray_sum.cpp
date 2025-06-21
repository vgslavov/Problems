#include <vector>
#include <unordered_map>

// number: 560
// title: Subarray Sum Equals K
// url: https://leetcode.com/problems/subarray-sum-equals-k/
// difficulty: medium
// tags: array, hash table, prefix sum

// constraints:
// 1 <= nums.length <= 2 * 10^4
// -1000 <= nums[i] <= 1000
// -107 <= k <= 10^7

// non-solution: prefix sum with brute force
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

// solution: Leetcode prefix sum + unordered_map
// complexity:
// run-time: O(n)
// space: O(n)
int subarraySum2(const std::vector<int>& nums, int k)
{
    int prefixSum = 0;
    int ans = 0;

    // prefix sum to count
    std::unordered_map<int, int> counts;
    // edge case: -1 index of prefix sum is 0
    counts[0] = 1;

    for (const auto& n : nums) {
        // build prefix sum but don't store intermediate results
        prefixSum += n;
        // prefixSum - diff = k
        int diff = prefixSum - k;
        
        auto it = counts.find(diff);            
        if (it != counts.end()) {
            ans += counts[diff];
        }

        ++counts[prefixSum]; 
    }

    return ans;
}

// TODO: add unit tests