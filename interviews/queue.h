#include <algorithm>
#include <cstddef>
#include <iostream>
#include <stdexcept>
#include <vector>

// section: interview
// difficulty: easy
// tags: optiver

// constraints
// don't use C++ vector/list/deque's push_back(), etc.
// allocate a chunk of memory

// solution: EPI using vector
// complexity
// run-time: see below
// space: O(n)
const size_t MAX_SIZE = 100;

template
<typename T>
class MyQueue {
public:
    MyQueue()
    : d_capacity(MAX_SIZE)
    , d_front(0)
    , d_back(0)
    , d_size(0)
    {
        // resize to prevent having to allocate additional memory
        d_queue.resize(d_capacity);
    }

    MyQueue(size_t capacity)
    : d_capacity(capacity)
    , d_front(0)
    , d_back(0)
    , d_size(0)
    {
        d_queue.resize(d_capacity);
    }

    // run-time: O(1) amortized, O(n) worst-case
    void push(const T& value)
    {
        if (d_size == d_capacity) {
            // shift everything to left: O(n)
            std::rotate(d_queue.begin(), d_queue.begin() + d_front, d_queue.end());
            d_front = 0;
            d_back = d_size;

            // double size
            d_capacity *= 2;

            // double capacity: O(n) for copying
            d_queue.resize(d_capacity);
        }

        d_queue[d_back++] = value;
        ++d_size;
    }

    // run-time: O(1)
    T pop()
    {
        if (empty()) {
            throw std::length_error("empty queue");
        }

        int value = d_queue[d_front];
        d_queue[d_front++] = 0;
        --d_size;

        return value;
    }

    // run-time: O(1)
    T front() const
    {
        if (empty()) {
            throw std::length_error("empty queue");
        }

        return d_queue[d_front];
    }

    // run-time: O(1)
    bool empty() const { return d_size == 0; }

    // run-time: O(1)
    size_t size() const { return d_size; }

private:
    std::vector<T> d_queue;
    size_t d_capacity;
    size_t d_front;
    size_t d_back;
    size_t d_size;
};
