#include <cstdlib>
#include <string>

// number: 161
// section: meta
// difficulty: medium
// tags: two pointers, string, meta

// constraints
// 0 <= s.length, t.length <= 10^4
// s and t consist of lowercase letters, uppercase letters, and digits.

// complexity:
// run-time: O(n)
// space: O(1)
bool sameLength(const std::string& s, std::string& t)
{
    if (s.size() != t.size()) {
        return false;
    }

    for (int i = 0; i != s.size(); ++i) {
        // everything after diff char should be same
        if (s[i] != t[i]) {
            return s.substr(i+1, s.size()) == t.substr(i+1, t.size());
        }
    }

    return false;
}

// solution: leetcode using two pointers
// complexity
// run-time: O(min(n,m))
// space: O(1)
bool isOneEditDistance(const std::string& s, std::string& t)
{
    int lenDiff = s.size()-t.size();
    if (std::abs(lenDiff) > 1 || s == t) {
        return false;
    }

    if (s.size() == t.size()) {
        return sameLength(s, t);
    }

    int i = 0;
    int j = 0;
    int ndiff = 0;

    while (i < s.size() && j < t.size()) {
        if (s[i] == t[j]) {
            ++i;
            ++j;
            continue;
        }

        ++ndiff;

        if (ndiff > 1) {
            return false;
        }

        // skip extra char
        if (s.size() > t.size()) {
            ++i;
        } else {
            ++j;
        }
    }

    return true;
}
