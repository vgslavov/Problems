#include <algorithm>
#include <vector>

// number: 34
// section: binary search
// difficulty: medium
// tags: array, binary search, top 150, meta

// constraints
// 0 <= nums.length <= 10^5
// -10^9 <= nums[i] <= 10^9
// nums is a non-decreasing array.
// -10^9 <= target <= 10^9

// complexity
// run-time: O(log n)
// space: O(1)
int binarySearch(const std::vector<int>& nums, int target)
{
    if (nums.empty()) {
        return -1;
    }

    int left = 0;
    int right = nums.size() - 1;

    while (left <= right) {
        int mid = left + (right-left) / 2;

        if (nums[mid] == target) {
            return mid;
        } else if (nums[mid] < target) {
            left = mid+1;
        } else {
            right = mid-1;
        }
    }

    return left;
}

// solution: manual binary search + two pointers
// complexity
// run-time: O(log n) average, O(n), if all duplicates
// space: O(1)
std::vector<int> searchRange(const std::vector<int>& nums, int target)
{
    int left = binarySearch(nums, target);

    if (left < 0 || left >= nums.size() || nums[left] != target) {
        return std::vector<int>{-1,-1};
    }

    int right = left;

    while (0 < left && right < nums.size()-1) {
        if (nums[left-1] == target) {
            --left;
        }

        if (nums[right+1] == target) {
            ++right;
        } else {
            break;
        }
    }

    while (0 < left) {
        if (nums[left-1] != target) {
            break;
        }
        --left;
    }

    while (right < nums.size()-1) {
        if (nums[right+1] != target) {
            break;
        }
        ++right;
    }

    return std::vector<int>{left, right};
}

// solution: C++ lower_bound
// complexity
// run-time: O(log n) average, O(n), if all duplicates
// space: O(1)
std::vector<int> searchRange2(const std::vector<int>& nums, int target)
{
    auto lower = std::lower_bound(nums.begin(), nums.end(), target);

    if (lower == nums.end() || *lower != target) {
        return std::vector<int>{-1,-1};
    }

    int left = std::distance(nums.begin(), lower);
    int right = left;

    while (right < nums.size() && nums[right] == target) {
        ++right;
    }

    return std::vector<int>{left, right-1};
}
