#include <string>
#include <tuple>
#include <vector>

// number: 12
// title: Integer to Roman
// url: https://leetcode.com/problems/integer-to-roman/
// section: array / string
// difficulty: medium
// tags: hash table, math, string, top 150

// constraints:
// 1 <= num <= 3999

// solution: greedy
// complexity:
// time: O(1)
// space: O(1)
std::string int2Roman(int num)
{
    // use a vector, not a map as we need to iterate in order
    std::vector<std::tuple<std::string, int>> romans = {
        {"M",1000},
        {"CM",900},
        {"D",500},
        {"CD",400},
        {"C",100},
        {"XC",90},
        {"L",50},
        {"XL",40},
        {"X",10},
        {"IX",9},
        {"V",5},
        {"IV",4},
        {"I",1}
    };

    std::string ans;

    for (const auto& r : romans) {
        const std::string& roman = std::get<0>(r);
        const int arabic = std::get<1>(r);

        if (arabic > num) {
            continue;
        }

        int count = num / arabic;

        // std::string(count, roman); doesn't work as roman is not a char!
        for (int i = 0; i != count; i++) {
            ans += roman;
        }

        num -= arabic * count;
    }

    return ans;
}

// TODO: add unit tests