#include <algorithm>
#include <string>
#include <unordered_map>

// number: 3
// title: Longest Substring Without Repeating Characters
// url: https://leetcode.com/problems/longest-substring-without-repeating-characters/
// section: sliding window
// difficulty: medium
// tags: hash table, string, sliding window, top 150, meta

// constraints
// 0 <= s.length <= 5 * 10^4
// s consists of English letters, digits, symbols and spaces.
// w/o repeating chars

// solution: sliding window + dict
// complexity
// run-time: O(n)
// space: O(n)
int lengthOfLongestSubstring(const std::string& s)
{
    int ans = 0;
    int left = 0;
    std::unordered_map<int, int> counts;

    for (int right = 0; right != s.size(); ++right) {
        ++counts[s[right]];

        while (counts[s[right]] > 1) {
            --counts[s[left]];
            if (counts[s[left]] == 0) {
                counts.erase(s[left]);
            }

            ++left;
        }

        ans = std::max(ans, right-left+1);
    }

    return ans;
}

// TODO: add unit tests