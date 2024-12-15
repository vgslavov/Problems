#include <algorithm>
#include <cstddef>
#include <utility>

namespace notstd {

template <typename T>
class rule_of_five {
public:
    // default ctor
    rule_of_five(T* p = nullptr)
    : ptr(p) {}

    // I. dtor
    ~rule_of_five()
    {
        if (ptr) {
            delete ptr;
            ptr = nullptr;
        }
    }

    // II. copy ctor
    rule_of_five(const rule_of_five& other)
    : rule_of_five(other.ptr) {}

    // III. copy assign op
    rule_of_five& operator=(const rule_of_five& other)
    {
        if (this == &other) {
            return *this;
        }

        // copy ctor
        rule_of_five temp(other);
        std::swap(ptr, temp.ptr);

        return *this;
    }

    // IV. move ctor
    //rule_of_five(rule_of_five&& other) noexcept
    //rule_of_five(rule_of_five&& other)
    //: ptr(std::exchange(other.ptr, nullptr)) {}

    // V. move assign op
    //rule_of_five& operator=(rule_of_five&& other) noexcept
    rule_of_five& operator=(rule_of_five&& other)
    {
        rule_of_five temp(std::move(other));
        std::swap(ptr, temp.ptr);
        return *this;
    }

private:
    T* ptr;
};

} // namespace notstd
