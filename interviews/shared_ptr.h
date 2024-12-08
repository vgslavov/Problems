#include <atomic>
#include <cstddef>
#include <utility>

namespace notstd {

template <typename T>
class shared_ptr {
public:
    // default ctor
    shared_ptr() = default;

    // copy ctor
    shared_ptr(const shared_ptr<T>& rhs) {
        d_buf = rhs.d_buf;
        d_refCount = rhs.d_refCount;
        (*d_refCount)++;
    }

    // move ctor
    shared_ptr(shared_ptr<T>&& rhs) {
        d_buf = rhs.d_buf;
        rhs.d_buf = nullptr;

        d_refCount = rhs.d_refCount;
        rhs.d_refCount = nullptr;
    }

    // dtor
    ~shared_ptr() { reset(); }

    void reset() {
        if (!d_buf) {
            return;
        }

        delete d_buf;
        delete d_refCount;

        d_buf = nullptr;
        d_refCount = nullptr;
    }

    // copy assignment op
    shared_ptr<T>& operator=(const shared_ptr<T>& rhs) {
        // prevent self-assignment
        if (&rhs == this) {
            return *this;
        }

        // don't leak mem!
        reset();

        d_buf = rhs.d_buf;
        d_refCount = rhs.d_refCount;
        (*d_refCount)++;

        return *this;
    }

    // move assignment op
    shared_ptr<T>& operator=(shared_ptr<T>&& rhs) {
        if (&rhs ==  this) {
            return *this;
        }

        // don't leak mem!
        reset();

        d_buf = rhs.d_buf;
        rhs.d_buf = nullptr;

        d_refCount = rhs.d_refCount;
        rhs.d_refCount = nullptr;

        return *this;
    }

    T* get() { return d_buf; }

    T* operator->() { return get(); }

    T& operator*() { return *get(); }

private:
    T* d_buf{nullptr};

    // make ref count thread-safe
    std::atomic<size_t *> d_refCount{nullptr};
};

} // notstd namespace
