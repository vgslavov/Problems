#include <algorithm>
#include <iostream>
#include <map>
#include <vector>

// number: 1128
// title: Number of Equivalent Domino Pairs
// url: https://leetcode.com/problems/number-of-equivalent-domino-pairs/
// section: assessments
// difficulty: easy
// tags: array, hash table, counting, amazon

// constraints
// 1 <= dominoes.length <= 4 * 104
// dominoes[i].length == 2
// 1 <= dominoes[i][j] <= 9

// solution: dict + math.comb
// complexity
// run-time: O(n)
// space: O(n)
long long int dp(long long int i, std::map<long long int, long long int>& memo)
{
    // base case
    if (i <= 0) {
        return 1;
    }

    // check cache
    auto it = memo.find(i);
    if (it != memo.end()) {
        return memo[i];
    }

    // recurrence relation
    memo[i] = dp(i-1, memo)*i;

    return memo[i];
}

// complexity
// run-time: O(n)
// space: O(n)
// TODO: fix overflows
int combinations(long long int n, int k)
{
    std::map<long long int, long long int> memo;
    long long int ans = dp(n, memo) / (dp(n-k, memo) * dp(k, memo));

    return ans;
}

// solution: map + recursive DP comb
// complexity
// run-time: O(n)
// space: O(n)
int dominoPairs(std::vector<std::vector<int>>& dominoes)
{
    std::map<std::vector<int>, int> counts;

    for (auto pair : dominoes) {
        std::sort(pair.begin(), pair.end());
        auto it = counts.find(pair);
        if (it != counts.end()) {
            counts[pair] += 1;
        } else {
            counts[pair] = 1;
        }
    }

    int ans = 0;

    for (const auto& c : counts) {
        std::cout << "key: " << c.first[0] << "," << c.first[1]
                  << ", value:" << c.second << std::endl;
        ans += combinations(c.second, 2);
    }

    return ans;
}

// TODO: add unit tests
