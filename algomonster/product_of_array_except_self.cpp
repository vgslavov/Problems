#include <vector>

// tags: prefix sum

// solution: AlgoMonster in-place prefix & suffix running products
// complexity:
// run-time: O(n)
// space: O(n)
std::vector<int> productOfArrayExceptSelf(const std::vector<int>& nums)
{
    std::vector<int> ans(nums.size(), 1);

    // 1. calc fwd prefix running product
    int left = 1;
    for (size_t i = 0; i != nums.size(); ++i) {
        // init to running product to left of i
        ans[i] = left;

        // calc running product for next iteration
        left *= nums[i];
    }

    // 2. calc backwards/suffix running product
    int right = 1;
    for (size_t i = nums.size(); i != 0;) {
        // for reverse it
        --i;

        // multiply in running product to right of i
        ans[i] *= right;

        // calc running product for next iteration
        right *= nums[i];
    }

    return ans;
}