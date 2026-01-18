#include <vector>

template <typename T>
class Sorted_vector {
public:
    // default ctor
    Sorted_vector() = default;

    // dtor
    ~Sorted_vector() = default;

    // ctor: from vector
    Sorted_vector(const std::vector<T>& rhs);
    Sorted_vector(std::vector<T>&& rhs);

    // copy ctor
    Sorted_vector(const Sorted_vector& rhs) = default;

    // copy assing op
    Sorted_vector& operator=(const Sorted_vector& rhs) = default;

    // move ctor
    Sorted_vector(Sorted_vector&& rhs) noexcept = default;

    Sorted_vector& operator(Sorted_vector&& rhs) noexcept = default;

    // use ref qualifiers for overloading
    T& operator[](size_t i) & { return d_vector[i]; }
    const T& operator[](size_t i) const& { return d_vector[i]; }
    T operator[](size_t i) && { return std::move((*this)[i]); }

    // TODO: insert in sorted place
    void push_back(const T& item);
    void push_back(T&& item);

private:
    std::vector<T> d_vector;
};

template<typename T>
bool operator==(const Sorted_vector<T>& rhs, const Sorted_vector<T>& lhs);

template<typename T>
bool operator!=(const Sorted_vector<T>& rhs, const Sorted_vector<T>& lhs);
