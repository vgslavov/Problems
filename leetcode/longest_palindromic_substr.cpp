#include <algorithm>
#include <deque>
#include <string>
#include <string_view>

// number: 5
// title: Longest Palindromic Substring
// url: https://leetcode.com/problems/longest-palindromic-substring/
// section: meta
// difficulty: medium
// tags: meta, two pointers, string, dp, grind 75
// similar: 647

// constraints
// 1 <= s.length <= 1000
// s consist of only digits and English letters.

std::string expandCenter(const std::string& s, int left, int right)
{
    std::deque<char> ans;

    while (left >= 0 && right < s.length()) {
        // no match, stop
        if (s[left] != s[right]) {
            break;
        }

        // don't add itself
        if (left == right) {
            ans.push_back(s[left]);
        } else {
            ans.push_back(s[right]);
            ans.push_front(s[left]);
        }

        --left;
        ++right;
    }

    return std::string(ans.begin(), ans.end());
}

// solution: expand from center
// complexity
// run-time: O(n^2)
// space: O(n)
std::string longestPalindrome(const std::string& s)
{
    std::string ans;
    auto longest = [](const std::string_view s1, const std::string_view s2) {
        return s1.size() < s2.size();
    };

    for (size_t i = 0; i != s.size(); ++i) {
        // check single letter
        std::string singlel = expandCenter(s, i, i);
        // check double letter
        std::string doublel = expandCenter(s, i, i+1);

        // find longest string
        ans = std::max({ans,singlel,doublel}, longest);
    }

    return ans;
}

// TODO: solve using DP & add unit tests
