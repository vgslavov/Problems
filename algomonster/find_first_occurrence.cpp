#include <vector>

// tags: binary search

// complexity
// run-time: O(log n)
// space: O(1)
int find_first_occurrence(const std::vector<int>& v, int target)
{
    int left = 0;
    int right = v.size()-1;
    int first = -1;

    while (left <= right) {
        int mid = left + (right-left)/2;

        if (v[mid] == target) {
            first = mid;
            right = mid-1;
        } else if (v[mid] > target) {
            right = mid-1;
        } else {
            left = mid+1;
        }
    }

    return first;
}