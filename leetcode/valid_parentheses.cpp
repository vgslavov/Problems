#include <iostream>
#include <map>
#include <set>
#include <stack>
#include <string>

// number: 20
// title: Valid Parentheses
// url: https://leetcode.com/problems/valid-parentheses/
// section: stack
// difficulty: easy
// tags: string, stack, top 150

// constraints
// 1 <= s.length <= 10^4
// s consists of parentheses only '()[]{}'.

// solution: stack
// complexity
// run-time: O(n)
// space: O(n)
bool isValid(std::string s)
{
    std::stack<char> stack;
    std::map<char, char> close2open{{'}','{'},
                                    {')','('},
                                    {']','['}};

    std::set<char> opening{'{','(','['};

    for (size_t i = 0; i != s.size(); ++i) {
        // opening bracket
        auto it = opening.find(s[i]);
        if (it != opening.end()) {
            stack.push(s[i]);
            continue;
        }

        // closing bracket
        auto mit = close2open.find(s[i]);
        if (mit != close2open.end()) {
            if (stack.empty() || stack.top() != mit->second) {
                return false;
            } else {
                stack.pop();
            }
        } else {
            std::cout << "invalid char: " << s[i] << std::endl;
        }
    }

    return stack.empty();
}