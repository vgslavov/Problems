#include <vector>

// tags: binary search

// complexity:
// run-time: O(log n)
// space: O(1)
int findMinRotated(const std::vector<int>& v)
{
    int left = 0;
    int right = v.size()-1;
    int boundary = 0;

    while (left <= right) {
        int mid = left + (right-left)/2;

        // compare to last element:
        // min is to the left
        if (v[mid] <= v.back()) {
            // record first not larger
            boundary = mid;
            right = mid-1;
        } else {
            left = mid+1;
        }
    }

    return boundary;
}