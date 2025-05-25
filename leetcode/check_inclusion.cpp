#include <map>
#include <string>

// number: 567
// similar: 438
// title: Permutation in String
// url: https://leetcode.com/problems/permutation-in-string/
// section: meta 
// difficulty: medium
// tags: hash table, two pointers, string, sliding window, meta

// constraints
// 1 <= s1.length, s2.length <= 10^4
// s1 and s2 consist of lowercase English letters.

// solution: LeetCode solution of #438, sliding window + map
// complexity
// run-time: O(n^2)
// space: O(1) (only 26 letters per map)
bool checkInclusion(const std::string& s1, const std::string& s2)
{
    // s1 cannot be longer than s2 and be a permutation of s2
    if (s1.size() > s2.size()) {
        return false;
    }

    // use char as key, not string!
    std::map<char, int> s1map;

    // count the frequency of each character in s1
    for (size_t i = 0; i != s1.size(); ++i) {
        auto it = s1map.find(s1[i]);
        if (it != s1map.end()) {
            it->second += 1;
        } else {
            s1map[s1[i]] = 1;
        }
    }

    // sliding window counter
    std::map<char, int> winmap;
    int left = 0;

    for (size_t right = 0; right != s2.size(); ++right) {
        // count the frequency of each character in the current window
        auto it = winmap.find(s2[right]);
        if (it != winmap.end()) {
            it->second += 1;
        } else {
            winmap[s2[right]] = 1;
        }

        // window is smaller than s1
        if (right-left+1 < s1.size()) {
            continue;
        }

        // check if the current window is a permutation of s1
        if (winmap == s1map) {
            return true;
        }

        // remove the leftmost character from the window
        if (winmap[s2[left]] > 1) {
            winmap[s2[left]] -= 1;
        } else {
            winmap.erase(s2[left]);
        }

        // slide the window
        ++left;
    }

    return false;
}

// TODO: add unit tests