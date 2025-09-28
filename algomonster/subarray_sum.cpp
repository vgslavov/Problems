#include <unordered_map>
#include <vector>

// tags: prefix sum

// solution: prefix sum + map
// complexity:
// run-time: O(n)
// space: O(n)
std::vector<int> subarraySum(const std::vector<int>& v, int target)
{
    int currSum = 0;

    // key: prefix sum
    // value: index up to which prefix sum was calculated
    std::unordered_map<int, int> prefixSums;
    // empty array
    prefixSums[0] = 0;

    for (int i = 0; i != v.size(); ++i) {
        currSum += v[i];

        // sum([i, j]) = sum([0, j]) - sum([0, i-1])
        // 0-----[i<--------->j]---->
        // target = currSum - complement
        int complement = currSum - target;

        auto itr = prefixSums.find(complement);
        if (itr != prefixSums.end()) {
            // right-exclusive: [start, end)
            return std::vector<int>{prefixSums[complement], i+1};
        }

        prefixSums[currSum] = i+1;
    }

    return std::vector<int>{};
}