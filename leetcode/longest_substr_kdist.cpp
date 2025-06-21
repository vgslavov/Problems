#include <algorithm>
#include <iostream>
#include <limits>
#include <string>
#include <unordered_map>

// number: 340
// title: Longest Substring with At Most K Distinct Characters
// url: https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
// difficulty: medium
// tags: hash table, string, sliding window

// constraints:
// 1 <= s.length <= 5 * 10^4
// 0 <= k <= 50

// solution: Leetcode sliding window
// complexity:
// run-time: O(n)
// space: O(k)
int lengthOfLongestSubstringKDistinct(const std::string& s, int k)
{
    if (s.empty() || k == 0) {
        return 0;
    } else if (k >= s.size()) {
        return s.size();
    }

    int left = 0;
    int ans = std::numeric_limits<int>::min();
    std::unordered_map<char, int> counts;

    for (int right = 0; right != s.size(); ++right) {
        ++counts[s[right]];

        while (counts.size() > k) {
            auto it = counts.find(s[left]);
            if (it == counts.end()) {
                std::cout << "key not found: " << s[left] << std::endl;
                break;
            } else if (counts[s[left]] > 1) {
                --counts[s[left]];
            } else {
                counts.erase(s[left]);
            }

            ++left;
        }

        ans = std::max(ans, right-left+1);
    }

    return ans;
}

// TODO: add unit tests