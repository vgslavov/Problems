#include <vector>

// tags: binary search

// complexity
// run-time: O(log n)
// space: O(1)
int squareRoot(long int n)
{
    if (n == 0) {
        return 0;
    }

    // start at 1!
    int left = 1;
    int right = n;
    int ans = 0;

    while (left <= right) {
        int mid = left + (right-left)/2;
        long int squared = (long int)mid * mid;

        if (squared == n) {
            return mid;
        } else if (squared > n) {
            // record first not smaller
            ans = mid;
            right = mid-1;
        } else {
            left = mid+1;
        }
    }

    // square root is b/w ans & ans-1
    return ans-1;
}