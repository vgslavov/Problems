#include <algorithm>
#include <cmath>
#include <vector>

// number: 977
// section: assessments
// difficulty: easy
// tags: array, two pointers, sorting, meta
//
// constraints
// 1 <= nums.length <= 10^4
// -10^4 <= nums[i] <= 10^4
// nums is sorted in non-decreasing order.

// solution: two pointers
// complexity
// run-time: O(n)
// space: O(n)
std::vector<int> sortedSquares(const std::vector<int>& nums)
{
    std::vector<int> ans;
    int left = 0;
    int right = nums.size()-1;
    int square = 0;

    while (left <= right) {
        if (abs(nums[left]) < abs(nums[right])) {
            square = nums[right];
            --right;
        } else {
            square = nums[left];
            ++left;
        }

        ans.push_back(std::pow(square, 2));
    }

    std::reverse(ans.begin(), ans.end());

    return ans;
}

// TODO: add unit tests
