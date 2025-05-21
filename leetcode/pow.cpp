// number: 50
// title: Pow(x, n)
// url: https://leetcode.com/problems/powx-n/
// section: math
// difficulty: medium
// tags: math, recursion, top 150, meta

// constraints
// -100.0 < x < 100.0
// -2^31 <= n <= 2^31-1
// n is an integer.
// Either x is not zero or n > 0.
// -10^4 <= x^n <= 10^4

// solution: recursive binary exponentiation
// complexity
// run-time: O(log n)
// space: O(log n)
double pow(double x, long long int n)
{
    // base case
    if (n == 0) {
        return 1;
    // negative exponent
    } else if (n < 1) {
        return 1/pow(x, -n);
    }

    // n even: (x^2)^(n/2)
    if (n % 2 == 0) {
        return pow(x*x, n/2);
    // n odd: x*(x^2)^(n-1)/2
    } else {
        return x * pow(x*x, (n-1)/2);
    }
}

// solution: iterative binary exponentiation
// complexity
// run-time: O(log n)
// space: O(1)
double pow2(double x, long long int n)
{
    bool isneg = false;

    if (n == 0) {
        return 1;
    } else if (n < 0) {
        n *= -1;
        isneg = true;
    }

    double ans = 1;

    while (n != 0) {
        // n is odd
        if (n % 2 == 1) {
            ans *= x;
            n -= 1;
        }

        x *= x;
        n /= 2;
    }

    return isneg ? 1/ans : ans;
}
