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
        // safe to delete nullptr
        delete ptr;
        ptr = nullptr;
    }

    // copy ctor - handle nullptr case
    copy_swap(const copy_swap& other)
    : ptr(other.ptr ? new T(*other.ptr) : nullptr) {}

    // move ctor - direct pointer transfer
    copy_swap(copy_swap&& other) noexcept
    : ptr(other.ptr)
    {
        other.ptr = nullptr;
    }

    // assign op: by value & same for copy/move
    copy_swap& operator=(copy_swap other)
    {
        swap(*this, other);
        return *this;
    }

    // Use the commented std::swap version instead
    friend void swap(copy_swap& a, copy_swap& b) noexcept
    {
        using std::swap;
        swap(a.ptr, b.ptr);
    }

private:
    T* ptr = nullptr;
};

} // namespace notstd
