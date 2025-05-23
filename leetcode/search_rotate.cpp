#include <algorithm>
#include <vector>

// number: 33
// title: Search in Rotated Sorted Array
// url: https://leetcode.com/problems/search-in-rotated-sorted-array/
// section: binary search
// difficulty: medium
// tags: array, binary search, top 150, meta

// constraints
// 1 <= nums.length <= 5000
// -10^4 <= nums[i] <= 10^4
// All values of nums are unique.
// nums is an ascending array that is possibly rotated.
// -10^4 <= target <= 10^4

// complexity
// run-time: O(log n)
// space: O(1)
int findMax(const std::vector<int>& nums)
{
    if (nums.empty()) {
        return -1;
    } else if (nums.size() == 1) {
        return 0;
    } else if (nums.size() == 2) {
        return std::distance(
            nums.begin(),
            std::max_element(nums.begin(), nums.end()));
    }

    int len = nums.size();
    int left = 0;
    int right = len-1;

    while (left < right) {
        int mid = left + (right-left)/2;

        // out of bounds
        if (mid-1 < 0 || mid+1 > nums.size()-1) {
            break;
        // found max
        } else if (nums[mid-1] < nums[mid] && nums[mid] > nums[mid+1]) {
            return mid;
        // descending
        } else if (nums[mid] > nums[len-1]) {
            left = mid+1;
        // ascending
        } else {
            right = mid-1;
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

// solution: manual binary search + C++ lower_bound
// complexity
// run-time: O(log n)
// space: O(1)
int searchRotate(const std::vector<int>& nums, int target)
{
    if (nums.empty()) {
        return -1;
    }

    int maxIndex = findMax(nums);
    if (maxIndex == -1) {
        return -1;
    }

    auto targetIt = std::lower_bound(
            nums.begin(), nums.begin()+maxIndex, target);
    if (targetIt != nums.end() && *targetIt == target) {
        return std::distance(nums.begin(), targetIt);
    }

    targetIt = std::lower_bound(nums.begin()+maxIndex+1, nums.end(), target);
    if (targetIt != nums.end() && *targetIt == target) {
        return std::distance(nums.begin(), targetIt);
    }

    return -1;
}
