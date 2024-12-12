#include "vector.h"

TEST(Vector, First)
{
    notstd::vector<int> v;

    EXPECT_TRUE(v.empty());
}
