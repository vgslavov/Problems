#include "rule_of_three.h"

int main()
{
    // default ctor
    notstd::rule_of_three<int> rt;

    // copy ctor
    notstd::rule_of_three<int> rt2(rt);

    // copy ctor
    notstd::rule_of_three<int> rt3 = rt2;

    // copy assing op
    notstd::rule_of_three<int> rt4;
    rt4 = rt;

    return 0;
}
