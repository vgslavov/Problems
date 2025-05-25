#include <algorithm>
#include <vector>

// number: 162
// title: Find Peak Element
// url: https://leetcode.com/problems/find-peak-element/
// section: binary search
// difficulty: medium
// tags: array, binary search, top 150, meta

// constraints
// 1 <= nums.length <= 1000
// -2^31 <= nums[i] <= 2^31 - 1
// nums[i] != nums[i + 1] for all valid i.

// solution: binary search
// complexity
// run-time: O(log n)
// space: O(1)
int findPeakElement(const std::vector<int>& nums)
{
    int len = nums.size();

    if (nums.empty()) {
        return -1;
    } else if (len == 1) {
        return 0;
    } else if (len == 2) {
        return std::distance(
            nums.begin(),
            std::max_element(nums.begin(), nums.end()));
    }

    int left = 0;
    int right = len - 1;

    while (left < right) {
        int mid = left + (right - left)/2;

        // check bounds
        if (mid-1 < 0 || mid+1 >= len) {
            break;
        // peak
        } else if (nums[mid-1] < nums[mid] && nums[mid] > nums[mid+1]) {
            return mid;
        // ascending
        } else if (nums[mid-1] > nums[mid] && nums[mid] > nums[mid+1]) {
            right = mid-1;
        // descending
        } else {
            left = mid+1;
        }
    }

    // TODO: refactor
    // check if peak is 1st or last
    if (nums[0] > nums[right] && nums[0] > nums[1]) {
        return 0;
    } else if (nums[len-1] > nums[right] && nums[len-1] > nums[len-2]) {
        return len-1;
    }

    return right;
}

// TODO: add unit tests
