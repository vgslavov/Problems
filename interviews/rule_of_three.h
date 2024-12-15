#include <algorithm>
#include <cstddef>

namespace notstd {

template <typename T>
class rule_of_three {
public:
    // default ctor
    explicit rule_of_three(T* p = nullptr)
    : ptr(p) {}

    // I. dtor
    ~rule_of_three()
    {
        if (ptr) {
            delete ptr;
            ptr = nullptr;
        }
    }

    // II. copy ctor
    rule_of_three(const rule_of_three& other)
    : rule_of_three(other.ptr) {}

    // III. copy assign op
    rule_of_three& operator=(const rule_of_three& other)
    {
        if (this == &other) {
            return *this;
        }

        // copy ctor
        rule_of_three temp(other);
        std::swap(ptr, temp.ptr);

        return *this;
    }

private:
    T* ptr = nullptr;
};

} // namespace notstd
