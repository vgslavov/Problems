#include <vector>

// number: 88
// title: Merge Sorted Array 
// url: https://leetcode.com/problems/merge-sorted-array/
// section: array/string
// difficulty: easy
// tags: array, two pointers, sorting, top 150, meta

// constraints
// nums1.length == m + n
// nums2.length == n
// 0 <= m, n <= 200
// 1 <= m + n <= 200
// -10^9 <= nums1[i], nums2[j] <= 10^9

// solution: two pointers
// complexity
// run-time: O(m + n)
// space: O(m + n)
void merge_lists(
        std::vector<int>& nums1,
        int m,
        const std::vector<int>& nums2,
        int n)
{
    int i = 0;
    int j = 0;
    std::vector<int> merged;

    while (i < m && j < n) {
        if (nums1[i] < nums2[j]) {
            merged.push_back(nums1[i]);
            ++i;
        } else {
            merged.push_back(nums2[j]);
            ++j;
        }
    }

    while (i < m) {
        merged.push_back(nums1[i]);
        ++i;
    }

    while (j < n) {
        merged.push_back(nums2[j]);
        ++j;
    }

    nums1 = merged;
}

// TODO: add unit tests & solve in O(1) space complexity