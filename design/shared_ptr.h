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
    shared_ptr()
    : d_count(new std::atomic<size_t>(0)) {}

    // ctor
    explicit shared_ptr(T* ptr)
    {
        if (!d_ptr) {
            d_ptr = new T(*ptr);
            d_count = new std::atomic<size_t>(1);
        } else {
            d_count = new std::atomic<size_t>(0);
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
    shared_ptr(shared_ptr<T>&& rhs) noexcept
    : d_ptr(rhs.d_ptr)
    , d_count(rhs.d_count)
    {
        rhs.d_ptr = nullptr;
        rhs.d_count = nullptr;
    }

    // dtor
    ~shared_ptr() noexcept { reset(); }

    void reset(T* ptr = nullptr)
    {
        if (d_count && d_count->fetch_sub(1) == 1) {  // atomic decrement and check
            delete d_ptr;
            delete d_count;
        }
        
        if (ptr) {
            d_ptr = ptr;  // Don't copy-construct, take ownership
            d_count = new std::atomic<size_t>(1);
        } else {
            d_ptr = nullptr;
            d_count = nullptr;
        }
    }

    // copy assignment op
    shared_ptr<T>& operator=(const shared_ptr<T>& rhs)
    {
        if (&rhs == this) return *this;  // Essential for correctness
        
        // Increment first to handle self-assignment safely
        if (rhs.d_count) ++(*rhs.d_count);
        
        reset();  // Now safe to reset
        
        d_ptr = rhs.d_ptr;
        d_count = rhs.d_count;
        
        return *this;
    }

    // move assignment op
    shared_ptr<T>& operator=(shared_ptr<T>&& rhs) noexcept
    {
        // prevent self-assignment
        if (&rhs == this) return *this;

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
