#include <algorithm>
#include <cstddef>
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

namespace notstd {

template
<typename T>
class queue {
public:
    // default ctor
    queue() = default;

    // ctor
    queue(size_t capacity)
    : d_capacity(capacity)
    , d_size(0)
    , d_head(0)
    {
        d_queue.resize(d_capacity);
    }

    // dtor
    ~queue() = default;

    // TODO: add copy/move semantics

    // run-time: O(1) amortized, O(n) worst-case
    void push(const T& value) {
        // check if full
        if (d_size == d_capacity) {
            // shift everything to left: O(n)
            std::rotate(d_queue.begin(),
                        d_queue.begin() + d_head,
                        d_queue.end());

            d_head = 0;

            // double capacity
            d_capacity = (d_capacity == 0) ? 1 : d_capacity * 2;

            // double size: O(n) for copying
            d_queue.resize(d_capacity);
        }

        d_queue[(d_head + d_size) % d_capacity] = value;

        // update size
        ++d_size;
    }

    // run-time: O(1)
    void pop() {
        if (empty()) {
            throw std::length_error("empty queue");
        }

        // init
        d_queue[d_head] = 0;

        // update head
        d_head = (d_head + 1) % d_capacity;

        // update size
        --d_size;
    }

    // run-time: O(1)
    T front() const {
        if (empty()) {
            throw std::length_error("empty queue");
        }

        return d_queue[d_head];
    }

    // run-time: O(1)
    T back() const {
        if (empty()) {
            throw std::length_error("empty queue");
        }

        return d_queue[(d_head + d_size-1) % d_capacity];
    }

    // run-time: O(1)
    bool empty() const { return d_size == 0; }

    // run-time: O(1)
    size_t capacity() const { return d_capacity; }

    // run-time: O(1)
    size_t size() const { return d_size; }

private:
    std::vector<T> d_queue;
    size_t d_capacity = 0;
    size_t d_size = 0;
    size_t d_head = 0;
};

} // notstd namespace
