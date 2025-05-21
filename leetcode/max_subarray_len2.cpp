#include <algorithm>
#include <vector>
#include <unordered_map>

// number: 325
// title: Maximum Size Subarray Sum Equals k
// url: https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/
// section: meta
// difficulty: medium
// tags: array, hash table, prefix sum, meta

// constraints
// 1 <= nums.length <= 10^5
// -10^4 <= nums[i] <= 10^4
// -10^4 <= k <= 10^4

// solution: prefix sum + unodered_map
// complexity
// run-time: O(n)
// space: O(n)
int maxSubArrayLen2(std::vector<int>& nums, int k)
{
    if (nums.empty()) {
        return 0;
    }

    std::vector<long long> prefix{nums[0]};

    for (size_t i = 1; i != nums.size(); ++i) {
        prefix.push_back(prefix.back()+nums[i]);
    }

    // don't use map
    // don't overflow
    std::unordered_map<int, long long> prefix2index;
    long long ans = 0;

    for (long long i = 0; i != prefix.size(); ++i) {
        if (prefix[i] == k) {
            ans = i + 1;
        }

        long long sum = prefix[i] - k;
        auto it = prefix2index.find(sum);
        if (it != prefix2index.end()) {
            ans = std::max(ans, i-prefix2index[sum]);
        }

        // don't prebuild, because we need to find the first index of prefix[i]
        it = prefix2index.find(prefix[i]);
        if (it == prefix2index.end()) {
            prefix2index[prefix[i]] = i;
        }
    }

    return ans;
}

// TOOD: add test cases