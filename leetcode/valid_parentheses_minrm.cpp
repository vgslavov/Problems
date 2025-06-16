#include <iostream>
#include <set>
#include <stack>
#include <vector>

// number: 1249
// title: Minimum Remove to Make Valid Parentheses
// url: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
// section: meta
// difficulty: medium
// tags: stack, string

// constraints
// 1 <= s.length <= 10^5
// s[i] is either '(' , ')', or lowercase English letter.

// solution: stack + set
// complexity
// run-time: O(n)
// space: O(n)
std::string minRemoveToMakeValid(const std::string& s)
{
    std::stack<int> stack;
    std::set<int> idx2rm;

    // 1st pass: identify indices to remove
    for (size_t i = 0; i != s.size(); ++i) {
        if (std::isalpha(s[i])) {
            continue;
        // add opening to stack
        } else if (s[i] == '(') {
            stack.push(i);
        // pop closing from stack if not empty
        } else if (s[i] == ')') {
            if (!stack.empty()) {
                stack.pop();
            } else {
                idx2rm.insert(i);
            }
        } else {
            std::cout << "invalid char: " << s[i] << std::endl;
        }
    }

    // cover trailing ((
    while (!stack.empty()) {
        idx2rm.insert(stack.top());
        stack.pop();
    }

    std::vector<char> ans;
    // TODO: inits with `\u0000`?
    //std::vector<char> ans(s.size()-idx2rm.size());
    ans.reserve(s.size()-idx2rm.size());

    // 2nd pass: remove chars
    for (size_t i = 0; i != s.size(); ++i) {
        auto it = idx2rm.find(i);
        if (it != idx2rm.end()) {
            continue;
        }

        ans.push_back(s[i]);
    }

    // more efficient than string operator+?
    return std::string(ans.begin(), ans.end());
}

// TODO: add unit tests