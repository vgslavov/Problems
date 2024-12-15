#include <cstddef>
#include <utility>

namespace notstd {

template <typename T>
class unique_ptr {
public:
    // default ctor
    explicit unique_ptr(T* ptr = nullptr)
    : d_ptr(ptr) {}

    // dtor
    ~unique_ptr() { reset(); }

    // copy ctor
    unique_ptr(const unique_ptr& rhs) = delete;

    // copy assign op
    unique_ptr& operator=(const unique_ptr& rhs) = delete;

    // move ctor
    unique_ptr(unique_ptr&& rhs)
    : d_ptr(rhs.d_ptr)
    {
        rhs.d_ptr = nullptr;
    }

    // move assign op
    unique_ptr& operator=(unique_ptr&& rhs)
    {
        if (this == &rhs) {
            return *this;
        }

        reset();

        d_ptr = rhs.d_ptr;
        rhs.d_ptr = nullptr;

        return *this;
    }

    T* get() { return d_ptr; }

    T* operator->() { return get(); }

    T& operator*() { return *get(); }

    void reset(T* ptr = nullptr)
    {
        if (d_ptr) {
            delete d_ptr;
        }

        if (ptr) {
            d_ptr = ptr;
        } else {
            d_ptr = nullptr;
        }
    }

private:
    T* d_ptr = nullptr;
};

} // namespace notstd
