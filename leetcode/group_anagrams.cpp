#include <algorithm>
#include <map>
#include <string>
#include <vector>

// number: 49
// title: Group Anagrams
// url: https://leetcode.com/problems/group-anagrams/
// section: hashmap
// difficulty: medium
// tags: array, hash table, string, sorting, top 150, meta, citadel

// constraints
// k: len(strs[i])
// n: len(strs)
// 1 <= n <= 10^4
// 0 <= k <= 100
// strs[i] consists of lowercase English letters.

// solution: map + sort
// complexity
// run-time: O(n * k * log(k))
// space: O(n * k)
std::vector<std::vector<std::string>> groupAnagrams(std::vector<std::string>& strs)
{
    // have to use map: need to iterate
    std::map<std::string, std::vector<std::string>> freqs;

    for (auto& s: strs) {
        std::string org(s);
        std::sort(s.begin(), s.end());
        freqs[s].push_back(org);
    }

    std::vector<std::vector<std::string>> ans;

    // like d.items() in Python!
    for (const auto& k: freqs) {
        // push the value: vector
        ans.push_back(k.second);
    }

    return ans;
}

// TODO: add unit tests
