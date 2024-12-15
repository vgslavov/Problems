#include <atomic>
#include <cstddef>
#include <utility>

// section: interview
// difficulty: medium
// tags: raw ptrs, smart ptrs, threads, exceptions, ctc

// constraints
// can't use std::shared_ptr

// discussion
// thread safety
// exception safety
// self-assignment
// move semantics

// solution: raw ptr + std::atomic

namespace notstd {

template <typename T>
class shared_ptr {
public:
    // default ctor
    explicit shared_ptr(T* ptr = nullptr)
    : d_ptr(ptr)
    {
        if (d_ptr) {
            d_count = new std::atomic<size_t>(1);
        }
    }

    // copy ctor
    shared_ptr(const shared_ptr<T>& rhs)
    : d_ptr(rhs.d_ptr)
    , d_count(rhs.d_count)
    {
        ++(*d_count);
    }

    // move ctor
    shared_ptr(shared_ptr<T>&& rhs)
    : d_ptr(rhs.d_ptr)
    , d_count(rhs.d_count)
    {
        rhs.d_ptr = nullptr;
        rhs.d_count = nullptr;
    }

    // dtor
    ~shared_ptr() { reset(); }

    void reset(T* ptr = nullptr)
    {
        // only delete if last ptr!
        if (--(*d_count) == 0) {
            delete d_ptr;
            delete d_count;
        }

        if (ptr) {
            d_ptr = ptr;
            d_count = new std::atomic<size_t>(1);
        } else {
            d_ptr = nullptr;
            d_count = nullptr;
        }
    }

    // copy assignment op
    shared_ptr<T>& operator=(const shared_ptr<T>& rhs)
    {
        // prevent self-assignment
        if (&rhs == this) {
            return *this;
        }

        // don't leak mem!
        reset();

        d_ptr = rhs.d_ptr;
        d_count = rhs.d_count;
        ++(*d_count);

        return *this;
    }

    // move assignment op
    shared_ptr<T>& operator=(shared_ptr<T>&& rhs)
    {
        if (&rhs == this) {
            return *this;
        }

        reset();

        d_ptr = rhs.d_ptr;
        rhs.d_ptr = nullptr;

        d_count = rhs.d_count;
        rhs.d_count = nullptr;

        return *this;
    }

    T* get() { return d_ptr; }

    T* operator->() { return get(); }

    T& operator*() { return *get(); }

private:
    T* d_ptr = nullptr;

    // make ref count thread-safe
    std::atomic<size_t>* d_count = nullptr;
};

} // notstd namespace
