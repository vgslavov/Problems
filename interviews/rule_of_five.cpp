#include "rule_of_five.h"

int main()
{
    // default ctor
    notstd::rule_of_five<int> rf;

    // copy ctor
    notstd::rule_of_five<int> rf2(rf);

    // copy ctor
    notstd::rule_of_five<int> rf3 = rf2;

    // copy assign op
    notstd::rule_of_five<int> rf4;
    rf4 = rf;

    // move ctor
    notstd::rule_of_five<int> rf5(std::move(rf2));

    // move assign op
    notstd::rule_of_five<int> rf6;
    rf6 = std::move(rf4);

    return 0;
}
