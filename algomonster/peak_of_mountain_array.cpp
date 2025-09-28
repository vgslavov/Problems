#include <vector>

// tags: binary search

// complexity
// run-time: O(log n)
// space: O(1)
int peakOfMountainArray(const std::vector<int>& v)
{
    int left = 0;
    int right = v.size()-1;
    int boundary = 0;

    while (left <= right) {
        int mid = left + (right-left)/2;

        // either found peak or it's to the left
        if (v[mid] > v[mid+1]) {
            boundary = mid;
            right = mid-1;
        } else {
            left = mid+1;
        }
    }

    return boundary;
}