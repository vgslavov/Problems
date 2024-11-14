#include <map>
#include <string>

// number: 383
// section: hashmap
// difficulty: easy
// tags: hash table, string, counting, top 150

// constraints
// 1 <= ransom_note.length, magazine.length <= 10^5
// ransom_note and magazine consist of lowercase English letters.

// complexity
// run-time: O(m+n), slow
// space: O(m)
bool canConstruct(std::string ransomNote, std::string magazine) {
    std::map<char, int> freqs;

    for (const auto& c : magazine) {
        const auto iter = freqs.find(c);

        if (iter != freqs.end()) {
            freqs[c] += 1;
        } else {
            freqs[c] = 1;
        }
    }

    for (const auto& c : ransomNote) {
        auto iter = freqs.find(c);
        if (iter == freqs.end() or freqs[c] == 0) {
            return false;
        }
        --freqs[c];
    }

    return true;
}
