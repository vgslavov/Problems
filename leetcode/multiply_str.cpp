#include <string>

// number: 43
// title: Multiply Strings
// url: https://leetcode.com/problems/multiply-strings/
// section: meta
// difficulty: medium
// tags: math, string, simulation, meta

// constraints
// 1 <= num1.length, num2.length <= 200
// num1 and num2 consist of digits only.
// Both num1 and num2 do not contain any leading zero, except the number 0 itself.

// complexity
// run-time: O(log n)
// space: O(1)
std::string int2str(unsigned long long int n)
{
    if (n == 0) {
        return "0";
    }

    std::string s;

    while (n > 0) {
        long long int d = n % 10;
        s += std::to_string(d);
        n /= 10;
    }

    std::reverse(s.begin(), s.end());
    return s;
}

// complexity
// run-time: O(n)
// space: O(1)
unsigned long long int str2int(const std::string& s)
{
    unsigned long long int digit = 1;
    unsigned long long int n = 0;

    // reversed!
    for (size_t i = s.size(); i != 0;) {
        --i;
        n += (s[i] - '0') * digit;
        digit *= 10;
    }

    return n;
}

// solution: str 2 int 2 str
// complexity
// run-time: O(n+m)
// space: O(1)
// TODO: fix overflow
std::string multiply(const std::string& num1, const std::string& num2)
{
    if (num1.empty() || num2.empty()) {
        return "";
    }

    return int2str(str2int(num1)*str2int(num2));
}
