#include <bitset>

// number: 67
// section: bit manipulation
// difficulty: easy
// tags: math, string, bit manipulation, simulation, top 150, meta

// constraints
// 1 <= a.length, b.length <= 10^4
// a and b consist only of '0' or '1' characters.
// Each string does not contain leading zeros except for the zero itself.

// solution: Leetcode, C++ stoi/bitset & bitwise operators
// run-time: O(n+m)
// space: O(max(n,m))
std::string addBinary(const std::string& a, const std::string& b) {
    int x = std::stoi(a, nullptr, 2);
    int y = std::stoi(b, nullptr, 2);

    while (y != 0) {
        int answer = x ^ y;
        int carry = (x & y) << 1;
        x = answer;
        y = carry;
    }

    std::string ans = std::bitset<8>(x).to_string();

    return ans.erase(0, ans.find_first_not_of("0"));
}
