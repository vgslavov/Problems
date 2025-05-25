#include <string>

// number: 58
// title: Length of Last Word
// url: https://leetcode.com/problems/length-of-last-word/
// section: array/string
// difficulty: easy
// tags: string, top 150

// constraints
// 1 <= s.length <= 10^4
// s consists of only English letters and spaces ' '
// There will be at least one word in s

// solution: reversed
// complexity
// run-time: O(n)
// space: O(1)
int lengthOfLastWord(const std::string& s)
{
    int count = 0;

    for (size_t i = s.size(); i != 0;) {
        --i;
        if (std::isalpha(s[i])) {
            ++count;
        } else if (count) {
            break;
        }
    }

    return count;
}

// TODO: add unit tests