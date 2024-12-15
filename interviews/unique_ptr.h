#include <cstddef>
#include <utility>

namespace notstd {

template <typename T>
class unique_ptr {
public:
    // default ctor
    // don't throw!
    explicit unique_ptr(T* ptr = nullptr) noexcept
    : d_ptr(ptr) {}

    // dtor
    ~unique_ptr() { reset(); }

    // copy ctor
    // don't copy!
    unique_ptr(const unique_ptr& rhs) = delete;

    // copy assign op
    // don't copy!
    unique_ptr& operator=(const unique_ptr& rhs) = delete;

    // move ctor
    // don't throw!
    unique_ptr(unique_ptr&& rhs) noexcept
    : d_ptr(rhs.d_ptr)
    {
        rhs.d_ptr = nullptr;
    }

    // move assign op
    // don't throw!
    unique_ptr& operator=(unique_ptr&& rhs) noexcept
    {
        if (this == &rhs) return *this;

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
