#include <unordered_map>
#include <vector>

// number: 128
// title: Longest Consecutive Sequence
// url: https://leetcode.com/problems/longest-consecutive-sequence/
// section: hashmap
// difficulty: medium
// tags: array, hash table, union find, top 150

// constraints
// k = max(nums)
// n = len(nums)
// 0 <= n <= 10^5
// -10^9 <= nums[i] <= 10^9

// complexity
// run-time: O(n)
// space: O(1)
int calcSeq(int k, std::unordered_map<int, int>& counts)
{
    int length = 0;
    auto it = counts.find(k);

    while (it != counts.end()) {
        // visit
        counts[k] = 0;

        // check if next number in sequence
        ++k;
        it = counts.find(k);

        ++length;
    }

    return length;
}

// solution: unordered_map
// complexity
// run-time: O(n+k*n) ~ O(n*k)
// space: O(k)
int longestConsecutive(const std::vector<int>& nums)
{
    if (nums.empty()) {
        return 0;
    }

    std::unordered_map<int, int> counts;
    for (const auto & n : nums) {
        ++counts[n];
    }

    int ans = 0;

    for (auto & p : counts) {
        // skip 0 counts
        if (!p.second) {
            continue;
        }

        // skip if in same seq
        auto it = counts.find(p.first-1);
        if (it != counts.end()) {
            continue;
        }

        ans = std::max(ans, calcSeq(p.first, counts));
    }

    return ans;
}

// TODO: add unit tests