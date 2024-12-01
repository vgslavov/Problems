#include <map>
#include <string>

// number: 791
// section: assessment
// difficulty: medium
// tags: hash table, string, sorting, meta

// constraints
// len(order): m
// len(s): n
// 1 <= m <= 26
// 1 <= n <= 200
// order and s consist of lowercase English letters.
// All the characters of order are unique.

// solution: map
// complexity
// run-time: O(n+m)
// space: O(n)
std::string customSort(const std::string& order, const std::string& s)
{
    // have to use map, not unordered_map due to key sorting
    std::map<char, int> counts;

    // O(n)
    for (const auto& c : s) {
        auto it = counts.find(c);
        if (it != counts.end()) {
            counts[c] += 1;
        } else {
            counts[c] = 1;
        }
    }

    std::string ans;

    // O(m)
    for (const auto& c : order) {
        auto it = counts.find(c);
        if (it != counts.end()) {
            ans += std::string(it->second, c);
            counts[c] = 0;
        }
    }

    // no need to sort, already sorted by key
    for (const auto& item : counts) {
        if (item.second) {
            ans += std::string(item.second, item.first);
            counts[item.first] = 0;
        }
    }

    return ans;
}

// TODO: add unit tests
