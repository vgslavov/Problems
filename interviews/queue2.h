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
            d_buf[i] = rhs.d_buf[i];
        }
    }

    // copy assign op
    queue& operator=(const queue& rhs)
    {
        // not necessary
        if (this == &rhs) return *this;

        clear();
        reserve(rhs.size());

        for (size_t i = 0; i != rhs.size(); ++i) {
            d_buf[i] = rhs.d_buf[i];
        }

        d_size = rhs.size();

        return *this;
    }

    //move ctor: default
    //queue(queue&& rhs) noexcept = default;

    // move ctor: manual
    queue(queue&& rhs) noexcept
    : d_capacity(rhs.d_capacity)
    , d_size(rhs.d_size)
    , d_head(rhs.d_head)
    , d_buf(std::move(rhs.d_buf))
    {
        rhs.d_capacity = 0;
        rhs.d_size = 0;
        rhs.d_head = 0;
        rhs.d_buf.reset();
    }

    // move assign op
    queue& operator=(queue&& rhs) noexcept
    {
        if (this == &rhs) return *this;

        d_capacity = rhs.d_capacity;
        rhs.d_capacity = 0;

        d_size = rhs.d_size;
        rhs.d_size = 0;

        d_head = rhs.d_head;
        rhs.d_head = 0;

        d_buf = std::move(rhs.d_buf);

        return *this;
    }

    void reserve(size_t capacity)
    {
        if (capacity <= d_capacity) {
            return;
        }

        auto newBuf = std::make_unique<T[]>(capacity);

        for (size_t i = 0; i != d_size; ++i) {
            newBuf[i] = std::move_if_noexcept(d_buf[i]);
        }

        d_buf = std::move(newBuf);
        d_capacity = capacity;
    }

    void push(const T& item)
    {
        if (d_capacity == d_size) {
            reserve(d_capacity == 0 ? 1 : d_capacity * 2);
        }

        d_buf[(d_head + d_size) % d_capacity] = item;
        ++d_size;
    }

    void push(T&& item)
    {
        if (d_capacity == d_size) {
            reserve(d_capacity == 0 ? 1 : d_capacity * 2);
        }

        d_buf[(d_head + d_size) % d_capacity] = std::move(item);
        ++d_size;
    }

    void pop()
    {
        if (empty()) {
            throw std::length_error("empty queue");
        }

        d_head = (d_head + 1) % d_capacity;
        --d_size;
    }

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

    void clear()
    {
        d_size = 0;
        d_head = 0;
        d_buf.reset();
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
