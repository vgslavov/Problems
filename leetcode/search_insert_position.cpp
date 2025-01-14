#include <vector>

// number: 35
// section: binary search
// difficulty: easy
// tags: array, binary search, top 150

// constraints
// 1 <= nums.length <= 10^4
// -10^4 <= nums[i] <= 10^4
// nums contains distinct values sorted in ascending order.
// -10^4 <= target <= 10^4

// solution: binary search
// complexity
// run-time: O(log n)
// space: O(1)
int searchInsert(const std::vector<int>& nums, int target)
{
    int left = 0;
    int right = nums.size()-1;

    // outside range
    if (nums.empty() || target < nums[0]) {
        return 0;
    } else if (target > nums.back()) {
        return nums.size();
    }

    while (left <= right) {
        int mid = left + (right-left)/2;

        if (target == nums[mid]) {
            return mid;
        } else if (target > nums[mid]) {
            left = mid+1;
        } else {
            right = mid-1;
        }
    }

    return left;
}
