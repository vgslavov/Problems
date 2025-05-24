// number: 69
// title: Sqrt(x)
// url: https://leetcode.com/problems/sqrtx/
// section: math
// difficulty: easy
// tags: math, binary search, top 150, citadel

// constraints
// 0 <= x <= 2^31 - 1

// long int: prevent overflow when squaring!
bool check(int x, long int k) {
    return k*k <= x;
}

// solution: binary search
// complexity
// run-time: O(log n)
// space: O(1)
int mySqrt(int x)
{
    // start at 1!
    int left = 1;
    int right = x;

    while (left <= right) {
        long int mid = left + (right-left) / 2;

        if (check(x, mid)) {
            left = mid+1; 
        } else {
            right = mid-1;
        }
    }

    // return right!
    return right;
}
