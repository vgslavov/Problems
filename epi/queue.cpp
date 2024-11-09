#include <cstddef>
#include <iostream>
#include <stdexcept>
#include <vector>

// section: interview
// difficulty: easy
// tags: optiver

// constraints
// don't use C++ list/deque's push_back(), etc.

// solution: epi using vector
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
        d_queue.reserve(d_capacity);
    }

    MyQueue(size_t capacity)
    : d_capacity(capacity)
    , d_front(0)
    , d_back(0)
    , d_size(0)
    {
        d_queue.reserve(d_capacity);
    }

    void push(const T& value)
    {
        if (d_size == d_capacity) {
            // shift left
            std::rotate(d_queue.begin(), d_queue.begin() + d_front, d_queue.end());
            d_front = 0;
            d_back = d_size;

            // double size
            d_capacity *= 2;
            d_queue.resize(d_capacity);
        }

        d_queue[d_back++] = value;
        ++d_size;
    }

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

    T front() const
    {
        if (empty()) {
            throw std::length_error("empty queue");
        }

        return d_queue[d_front];
    }

    bool empty() const { return d_size == 0; }

    size_t size() const { return d_size; }

private:
    std::vector<T> d_queue;
    size_t d_capacity;
    size_t d_front;
    size_t d_back;
    size_t d_size;
};
