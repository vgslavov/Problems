#include <cctype>
#include <deque>
#include <iostream>
#include <string>
#include <vector>

// number: 151
// section: array/string
// difficulty: medium
// tags: two pointers, string, top 150, leetcode 75

// constraints
// 1 <= s.length <= 10^4
// s contains English letters (upper-case and lower-case), digits, and spaces ' '.
// There is at least one word in s.

// solution: deque
// complexity
// run-time: O(n)
// space: O(n)
std::string reverseWords(const std::string& s)
{
    std::deque<std::string> queue;
    std::string word;

    for (size_t i = 0; i != s.length(); ++i) {
        if (std::isspace(s[i])) {
            if (word.empty()) {
                continue;
            }

            queue.push_front(word);
            word = "";
        } else if (std::isalnum(s[i])) {
            word += s[i];
        } else {
            std::cerr << "invalid input" << std::endl;
        }
    }

    if (!word.empty()) {
        queue.push_front(word);
    }

    std::string ans;

    for (auto cit = queue.begin(); cit != queue.end(); ++cit) {
        ans += *cit;

        if (cit != queue.end()-1) {
            ans += " ";
        }
    }

    return ans;
}
