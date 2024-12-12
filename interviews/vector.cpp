#include "vector.h"

#include <cassert>
#include <iostream>

int main()
{
    notstd::vector<int> v1;
    int size = 100;

    for (int i = 0; i != size; ++i) {
        v1.push_back(i);
    }

    v1[0] = 999;

    notstd::vector<int> v2(v1);
    assert(v1.size() == v2.size());

    notstd::vector<int> v3;
    assert(v3.empty());

    v3 = v1;
    assert(v1.size() == v3.size());

    for (size_t i = 0; i != v1.size(); ++i) {
        std::cout << "v1: " << v1[i]
                  << ", v2: " << v2[i]
                  << ", v3: " << v3[i]
                  << std::endl;
    }

    v3.clear();
    assert(v3.empty());

    return 0;
}
