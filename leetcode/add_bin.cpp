#include <bitset>

// number: 67
// title: Add Binary
// url: https://leetcode.com/problems/add-binary/
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
// TODO: fix std::out_of_range exception
std::string addBinary(const std::string& a, const std::string& b) {
    long long x = std::stoll(a, nullptr, 2);
    long long y = std::stoll(b, nullptr, 2);

    while (y != 0) {
        int answer = x ^ y;
        int carry = (x & y) << 1;
        x = answer;
        y = carry;
    }

    std::string ans = std::bitset<8>(x).to_string();

    if (x == 0) {
        return "0";
    }

    return ans.erase(0, ans.find_first_not_of("0"));
}
