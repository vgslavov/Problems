#include <vector>

// tags: two pointers

// solution: two pointers, opposite direction
// complexity:
// run-time: O(n)
// space: O(1)
std::vector<int> twoSumSorted(const std::vector<int>& v, int target)
{
    int left = 0;
    int right = v.size()-1;

    while (left < right) {
        int twoSum = v[left] + v[right];

        if (twoSum == target) {
            return std::vector<int>{left,right};
        // decrease pointer to reduce sum
        } else if (twoSum > target) {
            --right;
        } else {
            ++left;
        }
    }

    return std::vector<int>{};
}