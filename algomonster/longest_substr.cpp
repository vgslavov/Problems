#include <algorithm>
#include <string>
#include <unordered_map>

// tags: sliding window
// leetcode: 3

// solution: sliding window, longest + map
// complexity:
// run-time: O(n)
// space: O(n)
int longestSubstr(const std::string& s)
{
    int left = 0;
    int ans = 0;
    std::unordered_map<char, int> currWin;

    for (int right = 0; right != s.size(); ++right) {
        ++currWin[s[right]];

        // loop of 1 :)
        while (currWin[s[right]] > 1) {
            --currWin[s[left]];
            ++left;
        }

        ans = std::max(ans, right-left+1);
    }

    return ans;
}