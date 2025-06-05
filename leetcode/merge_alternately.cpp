#include <string>

// number: 1768
// title: Merge Strings Alternately
// url: https://leetcode.com/problems/merge-strings-alternately/
// difficulty: easy
// tags: two pointers, string

// constraints:
// 1 <= word1.length, word2.length <= 100
// word1 and word2 consist of lowercase English letters.

// solution: two pointers
// complexity
// run-time: O(n+m)
// space: O(n+m)
std::string mergeAlternately(const std::string& word1, const std::string& word2)
{
    int i = 0;
    int j = 0;
    bool alternate = true;
    std::string ans;

    while (i < word1.size() && j < word2.size()) {
        if (alternate) {
            ans += word1[i];
            ++i;
        } else {
            ans += word2[j];
            ++j;
        }

        alternate = !alternate;
    }

    if (i < word1.size()) {
        ans += word1.substr(i, word1.size());
    } else {
        ans += word2.substr(j, word2.size());
    }

    return ans;
}

// TODO: add unit tests