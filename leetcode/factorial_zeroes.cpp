#include <map>

// number: 172
// section: math
// difficulty: medium
// tags: math, top 150

// constraints
// 0 <= n <= 10^4

// complexity
// run-time: O(n)
// space: O(n)
// uses a lot of mem
long long int dp(long long int i, std::map<long long int, long long int>& memo)
{
    // base case
    if (i == 0) {
        return 1;
    }

    // check cache
    auto it = memo.find(i);
    if (it != memo.end()) {
        return memo[i];
    }

    // recurrence relation
    memo[i] = i * dp(i-1, memo);

    return memo[i];
}

long long int factorial(int n)
{
    std::map<long long int, long long int> memo;
    return dp(n, memo);
}

// WIP solution: recursive
// complexity
// run-time: O(n)
// space: O(n)
// TODO: fix overflows
int factorialZeroes(int n)
{
    long long int ans = factorial(n);
    int count = 0;

    while (ans != 0) {
        if (ans % 10 == 0) {
            count += 1;
        } else {
            break;
        }

        ans /= 10;
    }

    return count;
}

// TODO: solve in O(log n) & add unit tests
