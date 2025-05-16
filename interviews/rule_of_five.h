#include <algorithm>
#include <cstddef>
#include <utility>

namespace notstd {

template <typename T>
class rule_of_five {
public:
    // default ctor
    rule_of_five()
    : ptr(new T) {}

    // ctor
    explicit rule_of_five(T* p)
    : ptr(new T(*p)) {}

    // I. dtor
    ~rule_of_five()
    {
        // safe to delete nullptr
        delete ptr;
        ptr = nullptr;
    }

    // II. copy ctor
    rule_of_five(const rule_of_five& rhs)
    : rule_of_five(rhs.ptr) {}

    // III. copy assign op
    rule_of_five& operator=(const rule_of_five& rhs)
    {
        // optional
        if (this == &rhs) return *this;

        // copy ctor
        rule_of_five temp(rhs);
        std::swap(ptr, temp.ptr);

        return *this;
    }

    // IV. move ctor
    rule_of_five(rule_of_five&& rhs) noexcept
    : ptr(std::exchange(rhs.ptr, nullptr)) {}

    // V. move assign op
    rule_of_five& operator=(rule_of_five&& rhs) noexcept
    {
        ptr = std::exchange(rhs.ptr, nullptr);
        // or
        //rule_of_five temp(std::move(rhs));
        //std::swap(ptr, temp.ptr);
        return *this;
    }

private:
    T* ptr;
};

} // namespace notstd
