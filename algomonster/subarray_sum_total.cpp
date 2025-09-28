#include <unordered_map>
#include <vector>

// tags: prefix sum

// solution: prefix sum + map
// complexity:
// run-time: O(n)
// space: O(n)
int subarraySumTotal(const std::vector<int>& v, int target)
{
    int ans = 0;
    int currSum = 0;

    // key: prefix sum so far
    // value: freq of prefix sum
    std::unordered_map<int, int> prefixSums;
    // empty subarray freq
    prefixSums[0] = 1;

    for (size_t i = 0; i != v.size(); ++i) {
        currSum += v[i];

        // sum([i, j]) = sum([0, j]) - sum([0, i-1])
        // 0-----[i<--------->j]---->
        // target = currSum - complement
        int complement = currSum - target;

        auto itr = prefixSums.find(complement);
        if (itr != prefixSums.end()) {
            ans += prefixSums[complement];
        }

        ++prefixSums[currSum];
    }

    return ans;
}