#include <string>

// number: 647
// similar: 5
// title: Palindromic Substrings
// url: https://leetcode.com/problems/palindromic-substrings/
// section: citadel
// difficulty: medium
// tags: two pointers, string, dp, citadel

// constraints
// 1 <= s.length <= 1000
// s consists of lowercase English letters.

// run-time: O(n)
int countPalindromes(const std::string& s, int left, int right)
{
    int ans = 0;

    while (left >= 0 && right < s.length()) {
        if (s[left] != s[right]) {
            break;
        }

        ++ans;
        --left;
        ++right;
    }

    return ans;
}

// solution: Leetcode expand around centers
// complexity
// run-time: O(n^2)
// space: O(1)
int countSubstrings(const std::string& s)
{
    int ans = 0;

    for (size_t i = 0; i != s.length(); ++i) {
        // single-letter palindromes: aba
        ans += countPalindromes(s, i, i);

        // double-letter palindromes: abba
        ans += countPalindromes(s, i, i+1);
    }

    return ans;
}

// TODO: add unit tests
