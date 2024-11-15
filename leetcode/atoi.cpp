#include <algorithm>
#include <cctype>
#include <limits>
#include <string>

// number: 8
// section: meta
// difficulty: medium
// tags: string, meta

// constraints
// 0 <= s.length <= 200
// s consists of English letters (lower-case and upper-case), digits (0-9),
// ' ', '+', '-', and '.'.

// solution: Leetcode + STL
// complexity
// run-time: O(n)
// space: O(1)
int myAtoi(const std::string& s)
{
    if (s.empty()) {
        return 0;
    }

    // rm whitespace
    s.erase(s.begin(), std::find_if(s.begin(), s.end(),
        [](unsigned char ch) { return !std::isspace(ch); }));

    // read sign
    int sign = 1;
    if (!s.empty() && s[0] == '-') {
        sign = -1;
        s.erase(0, 1);
    } else if (!s.empty() && s[0] == '+') {
        s.erase(0, 1);
    }

    // up to non-number
    for (size_t i = 0; i != s.size(); ++i) {
        if (!std::isdigit(s[i])) {
            s.erase(i, s.length());
            break;
        }
    }

    // TODO: use substr()?
    //s = s.substr(0, std::find_if(s.begin(), s.end(),
    //    [](unsigned char ch) { return !std::isdigit(ch); }));

    int num = 0;

    for (const auto& ch: s) {
        // distance from 0 in ASCII
        int digit = (ch - '0');

        // check overflow *before* calc
        if ((num > std::numeric_limits<int>::max() / 10) ||
            (num == std::numeric_limits<int>::max() / 10 &&
            digit > (std::numeric_limits<int>::max() % 10)))
        {
            return sign == 1 ?
                std::numeric_limits<int>::max()
                : std::numeric_limits<int>::min();
        }

        num = 10 * num + digit;
    }

    return num * sign;
}
