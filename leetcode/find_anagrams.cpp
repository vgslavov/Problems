#include <map>
#include <string>

// number: 438
// similar: 567
// title: Find All Anagrams in a String
// url: https://leetcode.com/problems/find-all-anagrams-in-a-string/
// section: meta
// difficulty: medium
// tags: hash table, string, sliding window, meta, grind 75

// constraints
// 1 <= s.length, p.length <= 3 * 10^4
// s and p consist of lowercase English letters.

// solution: LeetCode solution, sliding window + defaultdict
// complexity:
// run-time: O(n^2)
// space: O(1) (only 26 letters per map)
std::vector<int> findAnagrams(const std::string& s, const std::string& p) {
    std::vector<int> ans;

    if (p.size() > s.size()) {
        return ans;
    }

    // sliding window counter
    std::map<char, int> pmap;
    for (size_t i = 0; i != p.size(); ++i) {
        auto it = pmap.find(p[i]);
        if (it != pmap.end()) {
            pmap[p[i]] += 1;
        } else {
            pmap[p[i]] = 1;
        }
    }

    std::map<char, int> winmap;
    int left = 0;

    for (size_t right = 0; right != s.size(); ++right) {
        auto it = winmap.find(s[right]);
        if (it != winmap.end()) {
            winmap[s[right]] += 1;
        } else {
            winmap[s[right]] = 1;
        }

        // window is smaller than p
        if (right-left+1 < p.size()) {
            continue;
        }

        // check if the current window is a permutation of p
        if (winmap == pmap) {
            ans.push_back(left);
        }

        // remove the leftmost character from the window
        if (winmap[s[left]] > 1) {
            winmap[s[left]] -= 1;
        } else {
            winmap.erase(s[left]);
        }

        // sliding the window
        ++left;
    }

    return ans;
}

// TODO: add unit tests