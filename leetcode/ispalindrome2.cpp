#include <string>

// number: 680
// title: Valid Palindrome II
// url: https://leetcode.com/problems/valid-palindrome-ii/
// section: meta
// difficulty: easy
// tags: two pointers, string, greedy,  meta

// constraints
// 1 <= s.length <= 10^5
// s consists of lowercase English letters.

// complexity
// run-time: O(n)
// space: O(1)
bool checkPalindrome(const std::string& s, int i, int j) {
    while (i < j) {
        if (s[i] != s[j]) {
            return false;
        }

        ++i;
        --j;
    }

    return true;
}

// solution: Leetcode recursive two pointers
// complexity:
// run-time: O(n)
// space: O(1)
bool validPalindrome(const std::string& s) {
    int i = 0;
    int j = s.length()-1;

    while (i < j) {
        if (s[i] != s[j]) {
            // fix i or j and check neighboring characters
            return checkPalindrome(s, i, j-1) ||
                    checkPalindrome(s, i+1, j);
        }

        ++i;
        --j;
    }

    return true;
}
