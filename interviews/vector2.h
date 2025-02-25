#include <cstddef>
#include <memory>

// section: interview
// difficulty: medium
// tags: exceptions, mem

// constraints
// don't use C++ vector

// solution: manual mem management
// complexity
// run-time: see below
// space: O(n)

namespace notstd {

template <typename T>
class vector2 {
public:
    // default ctor
    vector2() = default;

    // copy ctor
    vector2(const vector2<T>& rhs)
    : d_capacity(rhs.size())
    , d_size(rhs.size())
    , d_buf(new T[rhs.size()])
    {
        for (size_t i = 0; i != d_size; ++i) {
            d_buf[i] = rhs[i];
        }
    }

    // move ctor: default
    vector2(vector2<T>&& rhs) noexcept
    : d_capacity(rhs.size())
    , d_size(rhs.size())
    , d_buf(rhs.d_buf)
    {
        for (size_t i = 0; i != d_size; ++i) {
            d_buf[i] = std::move(rhs[i]);
        }

        rhs.d_buf = nullptr;
        rhs.d_size = 0;
        rhs.d_capacity = 0;
    }

    // dtor
    ~vector2() noexcept { clear(); }

    // copy assign op.
    vector2<T>& operator=(const vector2<T>& rhs);

    // move assign op.
    vector2<T>& operator=(vector2<T>&& rhs) noexcept;

    void reserve(size_t capacity);

    void clear()
    {
        d_capacity = 0;
        d_size = 0;
        delete[] d_buf;
    }

    void push_back(const T& item);
    void push_back(T&& item);

    T& operator[](size_t i) & { return d_buf[i]; }
    const T& operator[](size_t i) const& { return d_buf[i]; }
    T operator[](size_t i) && { return std::move((*this)[i]); }

    size_t capacity() const { return d_capacity; }
    size_t size() const { return d_size; }
    bool empty() const { return d_size == 0; }
private:
    size_t d_capacity = 0;
    size_t d_size = 0;
    T* d_buf = nullptr;
};

template <typename T>
vector2<T>& vector2<T>::operator=(const vector2<T>& rhs)
{
    if (this == &rhs) {
        return *this;
    }

    clear();
    reserve(rhs.size());

    for (size_t i = 0; i != rhs.size(); ++i) {
        d_buf[i] = rhs[i];
    }

    d_size = rhs.size();

    return *this;
}

template <typename T>
vector2<T>& vector2<T>::operator=(vector2<T>&& rhs) noexcept
{
    assert(&rhs != this);

    clear();

    d_size = rhs.size();
    d_capacity = rhs.capacity();
    d_buf = rhs.d_buf;
    //d_buf = std::move(rhs.d_buf);

    rhs.d_size = 0;
    rhs.d_capacity = 0;
    rhs.d_buf = nullptr;

    return *this;
}

template <typename T>
void vector2<T>::reserve(size_t newCapacity)
{
    if (newCapacity <= d_capacity) {
        return;
    }

    T* newBuf = new T[newCapacity];

    for (size_t i = 0; i != d_size; ++i) {
        newBuf[i] = std::move_if_noexcept(d_buf[i]);
        //newBuf[i] = std::move(d_buf[i]);
    }

    //clear();
    d_buf = std::move(newBuf);
    d_capacity = newCapacity;
}

template <typename T>
void vector2<T>::push_back(const T& item)
{
    if (d_size >= d_capacity) {
        reserve((d_capacity == 0) ? 1 : d_capacity * 2);
    }

    d_buf[d_size++] = item;
}

template <typename T>
void vector2<T>::push_back(T&& item)
{
    if (d_size >= d_capacity) {
        reserve((d_capacity == 0) ? 1 : d_capacity * 2);
    }

    d_buf[d_size++] = std::move(item);
}

} // namespace notstd
