#include <utility>

namespace notstd {

template <typename T>
class copy_swap {
public:
    // ctor
    explicit copy_swap(T* p = nullptr)
    : ptr(p) {}

    // dtor
    ~copy_swap()
    {
        if (ptr) {
            delete ptr;
            ptr = nullptr;
        }
    }

    // copy ctor
    copy_swap(const copy_swap& other)
    : ptr(new T(*other.ptr)) {}

    // move ctor
    copy_swap(copy_swap&& other) { swap(*this, other); }

    // assign op: by value & same for copy/move
    copy_swap& operator=(copy_swap other)
    {
        swap(*this, other);
        return *this;
    }

    // swap
    //friend void swap(copy_swap& a, copy_swap& b)
    //{
    //    using std::swap;
    //    swap(a.ptr, b.ptr);
    //}

    // manual swap
    friend void swap(copy_swap& a, copy_swap& b)
    {
        copy_swap tmp(std::move(a));
        a = std::move(b);
        b = std::move(tmp);
    }

private:
    T* ptr = nullptr;
};

} // namespace notstd
