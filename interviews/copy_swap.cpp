#include "copy_swap.h"

int main()
{
    // default ctor
    notstd::copy_swap<int> cs;

    // TODO: seg fault
    // copy ctor
    notstd::copy_swap<int> cs2(cs);

    return 0;
}
