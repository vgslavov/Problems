#include <stdexcept>
#include <tuple>
#include <vector>

// number: 155
// section: stack
// difficulty: medium
// tags: stack, design, top 150

// constraints
// -2^31 <= val <= 2^31 - 1
// Methods pop, top and get_min operations will always be called on non-empty stacks.
// At most 3 * 10^4 calls will be made to push, pop, top, and get_min.

// complexity
// run-time: O(1) per op
// space: O(n)
class MinStack {
public:
    MinStack() {}

    void push(int val) {
        int cmin = val;
        if (!d_stack.empty()) {
            cmin = std::min(val, getMin());
        }
        d_stack.push_back(std::make_pair(val, cmin));
    }

    void pop() {
        if (d_stack.empty()) {
            throw std::length_error("empty stack");
        }

        d_stack.pop_back();
    }

    int top() {
        if (d_stack.empty()) {
            throw std::length_error("empty stack");
        }

        return std::get<0>(d_stack.back());
    }

    int getMin() {
        if (d_stack.empty()) {
            throw std::length_error("empty stack");
        }

        return std::get<1>(d_stack.back());        
    }
private:
    // tuple: value, current min
    std::vector<std::tuple<int, int>> d_stack;
};

// Your MinStack object will be instantiated and called as such:
MinStack* obj = new MinStack();
obj->push(val);
obj->pop();
int param_3 = obj->top();
int param_4 = obj->getMin();
