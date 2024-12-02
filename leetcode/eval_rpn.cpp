#include <iostream>
#include <stack>
#include <stdexcept>
#include <string>
#include <vector>

// number: 150
// section: stack
// difficulty: medium
// tags: array, math, stack, top 150, citadel

// constraints
// 1 <= tokens.length <= 10^4
// tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the
// range [-200, 200].

int apply(int left, int right, const std::string& op) {
    if (op == "+") {
        return right + left;
    } else if (op == "-") {
        return right - left;
    } else if (op == "*") {
        return right * left;
    } else if (op == "/") {
        return right / left;
    } else {
        std::cerr << "invalid op: " << op << std::endl;
        return 0;
    }

    return 0;
}

bool isoperator(const std::string& s) {
    if (s == "+" || s == "-" || s == "*" || s == "/") {
        return true;
    }

    return false;
}

// solution: stack
// complexity
// run-time: O(n)
// space: O(n)
int evalRPN(std::vector<std::string>& tokens)
{
    std::stack<int> stack;

    for (const auto& t : tokens) {
        if (isoperator(t) && stack.size() >= 2) {
            int first = stack.top();
            stack.pop();
            int second = stack.top();
            stack.pop();
            stack.push(apply(first, second, t));
            continue;
        }

        try {
            stack.push(std::stoi(t, nullptr, 10));
        } catch (std::invalid_argument const& ex) {
            std::cout << "invalid argument: t: " << t
                        << ", " << ex.what() << std::endl;
        } catch (std::out_of_range const& ex) {
            std::cout << "out of range: t: " << t
                        << ", " << ex.what() << std::endl;
        }
    }

    return !stack.empty() ? stack.top() : 0;
}

// TODO: solve recursively & add unit tests
