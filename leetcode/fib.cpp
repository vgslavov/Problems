#include <map>
#include <vector>

// number: 509
// title: Fibonacci Number
// url: https://leetcode.com/problems/fibonacci-number/
// section: assessments
// difficulty: easy
// tags: math, dp, recursion, memoization, microsoft

// constraints
// 0 <= n <= 30

// solution: recursive
// complexity
// run-time: O(n!), TLE
// space: O(n)
int fib(int n)
{
    if (n == 0 || n == 1) {
        return n;
    }

    return fib(n-1)+fib(n-2);
}

int dp(int i, std::map<int, int>& memo)
{
    // base cases
    if (i == 0 || i == 1) {
        return i;
    }

    // check cache
    auto it = memo.find(i);
    if (it != memo.end()) {
        return memo[i];
    }

    // recurrence relation
    memo[i] = dp(i-1, memo) + dp(i-2, memo);

    return memo[i];
}

// solution: top-down recursive DP using map for memoization
// complexity
// run-time: O(n)
// space: O(n)
int fib2(int n)
{
    std::map<int, int> memo;
    return dp(n, memo);
}

// solution: bottom up iterative DP
// complexity
// run-time: O(n)
// space: O(n)
int fib3(int n)
{
    // init
    std::vector<int> dp(n+1);

    // base case
    if (n == 0) {
        return 0;
    }

    dp[1] = 1;

    // recurrence relation
    for (int i = 2; i != n+1; ++i) {
        dp[i] = dp[i-1] + dp[i-2];
    }

    return dp[n];
}

// TODO: add unit tests
