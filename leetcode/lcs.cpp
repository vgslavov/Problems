#include <map>
#include <string>
#include <tuple>

// number: 1143
// title: Longest Common Subsequence
// url: https://leetcode.com/problems/longest-common-subsequence/
// section: dp (multi-d)
// difficulty: medium
// tags: string, dp

// constraints
// 1 <= text1.length, text2.length <= 1000
// text1 and text2 consist of only lowercase English characters.

int dp(int i,
       int j,
       const std::string& text1,
       const std::string& text2,
       std::map<std::tuple<int, int>, int>& memo)
{
    // base case
    if (i == text1.size() || j == text2.size()) {
        return 0;
    }

    // check cache
    const auto tuple = std::make_tuple(i,j);
    const auto& it = memo.find(tuple);
    if (it != memo.end()) {
        return it->second;
    }

    // recurrence relation
    // match
    if (text1[i] == text2[j]) {
        memo[tuple] = 1 + dp(i+1, j+1, text1, text2, memo);
    // no match
    } else {
        memo[tuple] = std::max(dp(i, j+1, text1, text2, memo),
                               dp(i+1, j, text1, text2, memo));
    }

    return memo[tuple];
}

// solution: Leetcode top-down recursive 2DP using map
// complexity
// run-time: O(n*m)
// space: O(n*m)
int lcs1(const std::string& text1, const std::string& text2)
{
    std::map<std::tuple<int,int>, int> memo;

    return dp(0, 0, text1, text2, memo);
}

// solution: Leetcode bottom-up iterative 2DP
// complexity
// run-time: O(n*m)
// space: O(n)
int lcs2(const std::string& text1, const std::string& text2)
{
    if (text1.empty() || text2.empty()) {
        return 0;
    }

    // init: add 1!
    std::vector<std::vector<int>> dp(
        text1.size()+1, std::vector<int>(text2.size()+1));

    // go backwards from last to first inclusive!
    for (int i = text1.size()-1; i >= 0; --i) {
        for (int j = text2.size()-1; j >= 0; --j) {
            // recurrence relations
            if (text1[i] == text2[j]) {
                dp[i][j] = 1 + dp[i+1][j+1];
            } else {
                dp[i][j] = std::max(dp[i][j+1], dp[i+1][j]);
            }
        }
    }

    // longest subseq stored in 1st el
    return dp[0][0];
}

// TODO: add unit tests
