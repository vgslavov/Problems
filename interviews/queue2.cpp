#include "queue2.h"

#include <cassert>
#include <iostream>

int main()
{
    notstd::queue<int> q1;
    assert(q1.empty());

    size_t size = 100;
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

    return 0;
}
