#include "unique_ptr.h"

#include <cassert>
#include <string>

int main()
{
    // ctor
    notstd::unique_ptr<int> sp1(new int(10));
    assert(*sp1.get() == 10);

    // copy ctor!
    //notstd::unique_ptr<int> sp2 = sp1;
    //assert(*sp2.get() == 10);

    // reset
    sp1.reset(new int(20));
    assert(*sp1.get() == 20);

    //notstd::unique_ptr<int> sp3;
    // copy assign op
    //sp3 = sp2;
    //assert(*sp3.get() == 10);

    // copy ctor
    //notstd::unique_ptr<int> sp4(sp3);
    //assert(*sp4.get() == 10);

    // move ctor
    notstd::unique_ptr<int> sp5(notstd::unique_ptr<int>(new int(10)));
    assert(*sp5.get() == 10);

    // TODO: fix seg fault
    // move ctor
    //notstd::unique_ptr<int> sp6(std::move(sp5));
    //assert(*sp6.get() == 10);

    //sp5.reset();
    //assert(sp5.get() == nullptr);

    // TODO: test move assign op

    return 0;
}
