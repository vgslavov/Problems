#include <deque>
#include <vector>

// number: 238
// title: Product of Array Except Self
// url: https://leetcode.com/problems/product-of-array-except-self/
// section: array/string
// difficulty: medium
// tags: array, prefix sum, top 150, meta

// constraints
// 2 <= nums.length <= 10^5
// -30 <= nums[i] <= 30
// The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
// integer.
// You must write an algorithm that runs in O(n) time and without using the
// division operation.

// solution: prefix sum + deque
// complexity
// run-time: O(n), slow!
// space: O(n)
std::vector<int> productExceptSelf(std::vector<int>& nums)
{
    std::vector<int> ans;

    if (nums.empty()) {
        return ans;
    }

    // forward
    std::vector<int> prefixSum1{1};

    for (size_t i = 1; i != nums.size(); ++i) {
        prefixSum1.push_back(prefixSum1.back() * nums[i-1]);
    }

    // backward
    std::deque<int> prefixSum2{1};

    for (size_t i = nums.size()-1; i != 0;) {
        --i;
        prefixSum2.push_front(prefixSum2.front() * nums[i+1]);
    }

    for (size_t i = 0; i != nums.size(); ++i) {
        ans.push_back(prefixSum1[i] * prefixSum2[i]);
    }

    return ans;
}

// TODO: solve in O(1) space & add unit tests
