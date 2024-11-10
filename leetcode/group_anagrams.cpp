#include <algorithm>
#include <map>
#include <string>
#include <vector>

// number: 49
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
        // TODO: use not in-place sort
        std::sort(s.begin(), s.end());
        auto iter = freqs.find(s);
        if (iter != freqs.end()) {
            freqs[s].push_back(org);
        } else {
            // create vector on the fly
            freqs.insert(std::make_pair(s, std::vector<std::string>{org}));
            // or use insert_or_assign() in C++17
        }
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
