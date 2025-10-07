#include "fact.h"

#include <gtest/gtest.h>

namespace fact {


TEST(Factorial, ReturnsFactorialOfInteger) {
    EXPECT_EQ(Factorial(0), 1);
    EXPECT_EQ(Factorial(1), 1);
    EXPECT_EQ(Factorial(2), 2);
    EXPECT_EQ(Factorial(3), 6);
}


}  // namespace fact
