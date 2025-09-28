#include <vector>

// tags: binary search

bool feasible(int num, int target)
{
    return num >= target;
}

// complexity:
// run-time: O(log n)
// space: O(1)
int firstNotSmaller(const std::vector<int>& v, int target)
{
    int left = 0;
    int right = v.size()-1;
    int first = -1;

    while (left <= right) {
        int mid = left + (right-left)/2;

        if (feasible(v[mid], target)) {
            first = mid;
            right = mid-1;
        } else {
            left = mid+1;
        }
    }

    return first;
}