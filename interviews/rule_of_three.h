#include <algorithm>
#include <cstddef>

namespace notstd {

template <typename T>
class rule_of_three {
public:
    // default ctor
    rule_of_three()
    : ptr(new T) {}

    explicit rule_of_three(T* p)
    : ptr(new T(*p)) {}

    // I. dtor
    ~rule_of_three()
    {
        if (ptr) {
            delete ptr;
            ptr = nullptr;
        }
    }

    // II. copy ctor
    rule_of_three(const rule_of_three& rhs)
    : rule_of_three(rhs.ptr) {}

    // III. copy assign op
    rule_of_three& operator=(const rule_of_three& rhs)
    {
        // optional
        if (this == &rhs) return *this;

        // copy ctor
        rule_of_three temp(rhs);
        std::swap(ptr, temp.ptr);

        return *this;
    }

private:
    T* ptr = nullptr;
};

} // namespace notstd
