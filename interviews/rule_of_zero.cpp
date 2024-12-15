#include "rule_of_zero.h"

#include <utility>

int main()
{
    // default ctor
    notstd::rule_of_zero rz;

    // copy ctor
    notstd::rule_of_zero rz2(rz);
    notstd::rule_of_zero rz3 = rz;

    // copy assign op
    rz = rz3;

    // move ctor
    notstd::rule_of_zero rz4(std::move(rz));

    // move assing op
    rz2 = std::move(rz3);

    return 0;
}
