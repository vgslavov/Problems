#include <stdexcept>
#include <vector>

// number: 232
// section: 
// difficulty: easy
// tags: stack, design, queue

// constraints
// 1 <= x <= 9
// At most 100 calls will be made to push, pop, peek, and empty.
// All the calls to pop and peek are valid.

// complexity
// run-time: see below
// space: O(n)
class MyQueue {
public:
    // run-time: O(1)
    void push(int x) {
        d_back.push_back(x);
    }

    // run-time: O(1) amortized, O(n) worst-case
    int pop() {
        if (empty()) {
            throw std::length_error("empty queue");
        }

        if (d_front.empty() && !back2front()) {
            throw std::runtime_error("failed to move back to front");
        }

        int value = d_front.back();
        d_front.pop_back();
        return value;
    }

    // run-time: O(1) amortized, O(n) worst-case
    int peek() {
        if (empty()) {
            throw std::length_error("empty queue");
        }

        if (d_front.empty() && !back2front()) {
            throw std::runtime_error("failed to move back to front");
        }

        return d_front.back();
    }

    // run-time: O(1)
    bool empty() {
        return d_front.empty() and d_back.empty();
    }

private:
    // run-time: O(n)
    bool back2front() {
        if (empty()) {
            return false;
        }

        while (!d_back.empty()) {
            d_front.push_back(d_back.back());
            d_back.pop_back();
        }

        return !d_front.empty();
    }
    std::vector<int> d_front;
    std::vector<int> d_back;
};

MyQueue* obj = new MyQueue();
obj->push(x);
int param_2 = obj->pop();
int param_3 = obj->peek();
bool param_4 = obj->empty();
