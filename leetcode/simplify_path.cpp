#include <iostream>
#include <string>
#include <stack>
#include <sstream>
#include <vector>

// number: 71
// title: Simplify Path
// url: https://leetcode.com/problems/simplify-path/
// section: stack
// difficulty: medium
// tags: string, stack, top 150, meta, me, citadel

// constraints
// 1 <= path.length <= 3000
// path consists of English letters, digits, period '.', slash '/' or '_'.
// path is a valid absolute Unix path.

// solution: stack
// complexity
// run-time: O(n)
// space: O(n)
std::string simplifyPath(const std::string& path)
{
    if (path.empty()) {
        return "";
    }

    std::stack<std::string> stack;
    std::string dir;
    char delimiter = '/';
    std::istringstream ss(path);

    while (std::getline(ss, dir, delimiter)) {
        // current or empty dir
        if (dir.empty() || dir == ".") {
            continue;
        // parent dir
        } else if (dir == "..") {
            if (!stack.empty()) {
                stack.pop();
            }
        // normal dir
        } else {
            stack.push(dir);
        }
    }

    std::string ans;
    // build path from stack in reverse order
    while (!stack.empty()) {
        ans = "/" + stack.top() + ans;
        stack.pop();
    }

    return ans.empty() ? "/" : ans;