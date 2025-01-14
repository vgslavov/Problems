#include <string>

// number: 28
// section: array/string
// difficulty: easy
// tags: two pointers, string, string matching, top 150

// constraints
// 1 <= haystack.length, needle.length <= 10^4
// haystack and needle consist of only lowercase English characters.

// solution: substr
// complexity
// run-time: O((n-m+1)*m)
// space: O(1)
int strStr(std::string haystack, std::string needle)
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

// TODO: solve using two pointers and add unit tests
