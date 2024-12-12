#include "shared_ptr.h"

#include <cassert>
#include <string>

int main()
{
    // ctor
    notstd::shared_ptr<int> sp1(new int(10));
    assert(*sp1.get() == 10);

    // copy assign op
    notstd::shared_ptr<int> sp2 = sp1;
    assert(*sp2.get() == 10);

    // reset
    sp1.reset(new int(20));
    assert(*sp1.get() == 20);
    assert(*sp2.get() == 10);

    notstd::shared_ptr<int> sp3;
    // copy assign op
    sp3 = sp2;
    assert(*sp3.get() == 10);

    return 0;
}
