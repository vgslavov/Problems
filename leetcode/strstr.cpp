#include <string>

// number: 28
// title: Find the Index of the First Occurrence in a String
// url: https://leetcode.com/problems/implement-strstr/
// section: array/string
// difficulty: easy
// tags: two pointers, string, string matching, top 150

// constraints
// 1 <= haystack.length, needle.length <= 10^4
// haystack and needle consist of only lowercase English characters.

// solution: substr
// complexity
// run-time: O(n*m)
// space: O(1)
int strStr(const std::string& haystack, const std::string& needle)
{
    if (haystack.empty() || needle.empty()) {
        return -1;
    } else if (haystack == needle) {
        return 0;
    }

    for (size_t i = 0; i != haystack.size(); ++i) {
        if (haystack.substr(i, needle.size()) == needle) {
            return i;
        }
    }

    return -1;
}

// non-solution: manual substr
// complexity
// run-time: O(n*m), TLE
// space: O(1)
int strStr2(const std::string& haystack, const std::string& needle) {
    if (haystack.empty() || needle.empty()) {
        return -1;
    } else if (haystack == needle) {
        return 0;
    }

    for (size_t i = 0; i != haystack.size()-needle.size()+1; ++i) {
        for (size_t j = 0; j != needle.size(); ++j) {
            // prevent index out of range
            if (i+j >= haystack.size() || haystack[i+j] != needle[j]) {
                break;
            }

            if (j == needle.size()-1) {
                return i;
            }
        }
    }

    return -1;
}

// TODO: solve using two pointers and add unit tests
