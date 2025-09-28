#include <vector>

// tags: prefix sum

// solution: prefix sum
// complexity:
// run-time: O(n) to build prefix sum, O(1) per query
// space: O(n)
int rangeSumQueryImmutable(const std::vector<int> nums, int left, int right)
{
    if (nums.empty()) {
        return 0;
    }

    std::vector<int> prefixSum;
    prefixSum.push_back(0);

    for (size_t i = 0; i != nums.size(); ++i) {
        prefixSum.push_back(prefixSum.back()+nums[i]);
    }

    return prefixSum[right+1]-prefixSum[left];
}

// solution: C++ partial_sum
// complexity:
// run-time: O(n) to build prefix sum, O(1) per query
// space: O(n)
int rangeSumQueryImmutable2(const std::vector<int> nums, int left, int right)
{
    if (nums.empty()) {
        return 0;
    }

    std::vector<int> prefixSum(nums.size()+1);
    prefixSum[0] = 0;
    std::partial_sum(nums.begin(), nums.end(), prefixSum.begin());

    return prefixSum[right+1]-prefixSum[left];
}