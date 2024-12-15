#include <cstddef>
#include <cstdio>
#include <memory>
#include <stdexcept>

namespace notstd {

template <typename T>
class queue {
public:
    // default ctor
    queue() = default;

    queue(size_t capacity)
    : d_capacity(capacity)
    , d_size(0)
    , d_head(0)
    , d_buf(std::make_unique<T[]>(capacity)) {}

    // dtor
    ~queue() = default;

    // copy ctor
    queue(const queue& rhs)
    : d_capacity(rhs.d_capacity)
    , d_size(rhs.d_size)
    , d_head(rhs.d_head)
    , d_buf(std::make_unique<T[]>(rhs.d_size))
    {
        for (size_t i = 0; i != d_size; ++i) {
            d_buf[i] = rhs[i];
        }
    }

    // copy assign op
    queue& operator=(const queue& rhs) = default;

    // move ctor
    queue(queue&& rhs) noexcept = default;

    // move assign op
    queue& operator=(queue&& rhs) noexcept = default;

    void reserve(size_t capacity) {}

    void push(const T& item)
    {
        if (d_capacity == d_size) {
            reserve(d_capacity == 0 ? 1 : d_capacity * 2);
        }

        // TODO
    }

    void pop() {}

    T front() const
    {
        if (empty()) {
            throw std::length_error("empty queue");
        }

        return d_buf[d_head];
    }

    T back() const
    {
        if (empty()) {
            throw std::length_error("empty queue");
        }

        // subtract 1!
        return d_buf[(d_head + d_size-1) % d_capacity];
    }

    bool empty() const { return d_size == 0; }

    size_t capacity() const { return d_capacity; }

    size_t size() const { return d_size; }

private:
    size_t d_capacity = 0;
    size_t d_size = 0;
    size_t d_head = 0;
    std::unique_ptr<T[]> d_buf;
};

} // namespace notstd
