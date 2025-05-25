#include <algorithm>
#include <vector>

// number: 153
// title: Find Minimum in Rotated Sorted Array
// url: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
// section: binary search
// difficulty: medium
// tags: array, binary search, top 150

// constraints
// n == nums.length
// 1 <= n <= 5000
// -5000 <= nums[i] <= 5000
// All the integers of nums are unique.
// nums is sorted and rotated between 1 and n times.

// solution: binary search
// complexity
// run-time: O(log n)
// space: O(1)
int findMin(const std::vector<int>& nums)
{
    if (nums.empty()) {
        return -1;
    } else if (nums.size() == 1) {
        return nums[0];
    } else if (nums.size() == 2) {
        return *std::min_element(nums.begin(), nums.end());
    }

    int left = 0;
    int right = nums.size()-1;

    // no =
    while (left < right) {
        int mid = left + (right-left)/2;

        if (mid > 0 && mid < nums.size() &&
            nums[mid-1] > nums[mid] && nums[mid] < nums[mid+1])
        {
            return nums[mid];
        // go right, rotation is there
        } else if (nums[mid] > nums.back()) {
            left = mid+1;
        } else {
            right = mid-1;
        }
    }

    return nums[left];
}

// TODO: add unit tests
