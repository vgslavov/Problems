#include <algorithm>
#include <map>
#include <set>
#include <string>
#include <vector>

// number: 819
// title: Most Common Word
// url: https://leetcode.com/problems/most-common-word/
// section: assessments
// difficulty: easy
// tags: array, hash able, string, counting, amazon

// constraints
// 1 <= paragraph.length <= 1000
// paragraph consists of English letters, space ' ', or one of the symbols: "!?',;.".
// 0 <= banned.length <= 100
// 1 <= banned[i].length <= 10
// banned[i] consists of only lowercase English letters.

// solution: manual tokenize + map + max_element
// complexity
// run-time: O(n)
// space: O(n)
std::string mostCommonWord(
                const std::string& paragraph,
                const std::vector<std::string>& banned)
{
    std::set<std::string> bannedSet(banned.begin(), banned.end());
    std::map<std::string, size_t> counts;
    using pair_type = decltype(counts)::value_type;
    std::string word;

    for (const auto & c : paragraph) {
        if (std::isalpha(c)) {
            word += std::tolower(c);
        } else if (!word.empty()) {
            // skip banned words
            auto it = bannedSet.find(word);
            if (it != bannedSet.end()) {
                word.clear();
                continue;
            }

            // count
            ++counts[word];
            word.clear();
        }
    }

    if (!word.empty()) {
        auto it = bannedSet.find(word);
        if (it == bannedSet.end()) {
            ++counts[word];
        }
    }

    // find the most common word
    auto ans = *std::max_element(
        counts.begin(), counts.end(),
        [ ](const pair_type& p1, const pair_type& p2) {
            return p1.second < p2.second;
        }
    );

    return ans.first;
}

// TODO: add unit tests