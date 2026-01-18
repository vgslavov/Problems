#include "queue2.h"

#include <cassert>
#include <iostream>

int main()
{
    // default ctor
    notstd::queue<int> q1;
    assert(q1.empty());

    size_t size = 100;
    // ctor
    notstd::queue<int> q2(size);
    assert(q2.capacity() == size);

    for (size_t i = 0; i != size; ++i) {
        q1.push(i);
    }

    assert(q1.size() == size);
    assert(q1.front() == 0);

    q1.pop();
    assert(q1.front() == 1);

    q1.pop();
    assert(q1.size() == 98);

    // copy ctor
    notstd::queue<int> q3(q1);
    assert(q3.size() == q1.size());

    // move ctor
    notstd::queue<int> q4(std::move(q1));
    assert(q4.size() == q3.size());

    // copy assign op
    q4 = q2;
    assert(q4.size() == q2.size());

    // move assign op
    //q2 = std::move(q3);
    //assert(q2.size() == size);

    return 0;
}
