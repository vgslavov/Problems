#include <cstdio>
#include <memory>

// section: interview
// difficulty: medium
// tags: exceptions, mem, sig

// constraints
// don't use C++ vector
// implement push_back

// solution: unique_ptr & move semantics
// complexity
// run-time: see below
// space: O(n)

// discussion
// * exception safety guarantees of push_back/reserve
// * move semantics

namespace notstd {

template <typename T>
class vector {
public:
    // default ctor
    vector() = default;

    // copy ctor
    vector(const vector<T>& rhs)
    : d_capacity(rhs.size())
    , d_size(rhs.size())
    , d_buf(std::make_unique<T[]>(rhs.size()))
    {
        for (size_t i = 0; i != d_size; ++i) {
            d_buf[i] = rhs[i];
        }
    }

    // move ctor: default
    vector(vector<T>&& rhs) = default;

    // move ctor: manual
    //vector(vector&& rhs) noexcept
    //: d_capacity(rhs.size())
    //, d_size(rhs.size())
    //, d_buf(std::move(rhs.d_buf)) {}

    // dtor
    ~vector() noexcept = default;

    // copy
    // run-time: O(1) amortized, O(n) worst-case
    void push_back(const T& item);

    // move
    // run-time: O(1) amortized, O(n) worst-case
    void push_back(T&& item);

    // use ref qualifiers for overloading
    T& operator[](size_t i) & { return d_buf[i]; }
    const T& operator[](size_t i) const& { return d_buf[i]; }
    T operator[](size_t i) && { return std::move((*this)[i]); }

    // use ref qualifiers for overloading
    T& at(size_t i) & {
        if (i >= d_size) {
            throw std::out_of_range("index out of range");
        }

        return d_buf[i];
    }

    const T& at(size_t i) const& {
        return const_cast<vector<T>&>(*this).at(i);
    }

    T at(size_t i) && { return std::move(at(i)); }

    // copy assignment op
    vector<T>& operator=(const vector<T>& rhs);
    // move assignment op
    vector<T>& operator=(vector<T>&& rhs) noexcept;

    void reserve(size_t capacity);

    void clear()
    {
        d_size = 0;
        d_buf.reset();
    }

    size_t capacity() const { return d_capacity; }
    size_t size() const { return d_size; }
    bool empty() const { return d_size == 0; }

private:
    // default member init
    size_t d_capacity = 0;
    size_t d_size = 0;
    std::unique_ptr<T[]> d_buf = nullptr;
};

template <typename T>
vector<T>& vector<T>::operator=(const vector<T>& rhs)
{
    // prevent self-assignment
    if (&rhs == this) {
        return *this;
    }

    // clear existing
    clear();

    // reserve capacity == size
    reserve(rhs.size());

    // copy
    for (size_t i = 0; i != rhs.size(); ++i) {
        d_buf[i] = rhs[i];
    }

    // set size
    d_size = rhs.size();

    return *this;
}

template <typename T>
vector<T>& vector<T>::operator=(vector<T>&& rhs) noexcept
{
    assert(&rhs != this);

    clear();

    d_size = rhs.size();
    d_capacity = rhs.capacity();
    d_buf = std::move(rhs.d_buf);

    rhs.d_size = 0;
    rhs.d_capacity = 0;
    rhs.d_buf = nullptr;

    return *this;
}

// exceptions
// * make_unique
// * moves
template <typename T>
void vector<T>::reserve(size_t newCapacity)
{
    if (newCapacity <= d_capacity) {
        return;
    }

    auto newBuf = std::make_unique<T[]>(newCapacity);

    for (size_t i = 0; i != d_size; ++i) {
        // guarantee strong exception safety (depending on T)
        newBuf[i] = std::move_if_noexcept(d_buf[i]);
        //newBuf[i] = std::move(d_buf[i]);
    }

    d_buf = std::move(newBuf);
    d_capacity = newCapacity;
}

// exceptions
// * reserve
template <typename T>
void vector<T>::push_back(const T& item)
{
    if (d_size >= d_capacity) {
        reserve((d_capacity == 0) ? 1 : d_capacity * 2);
    }

    d_buf[d_size++] = item;
}

// exceptions
// * reserve
// * move
template <typename T>
void vector<T>::push_back(T&& item)
{
    if (d_size >= d_capacity) {
        reserve((d_capacity == 0) ? 1 : d_capacity * 2);
    }

    d_buf[d_size++] = std::move(item);
}

} // notstd namespace
