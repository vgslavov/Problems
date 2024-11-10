// number: 69
// section: math
// difficulty: easy
// tags: math, binary search, top 150, citadel

// constraints
// 0 <= x <= 2^31 - 1

// solution: binary search
// complexity
// run-time: O(n)
// space: O(1)

// long int: prevent overflow when squaring!
bool check(int x, long int k) {
    if (k*k > x) {
        return false;
    }

    return true;
}

int mySqrt(int x) {
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
