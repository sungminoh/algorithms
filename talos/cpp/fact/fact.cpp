#include "fact.h"

namespace fact {


int Factorial(int n) {
    if (n == 0) {
        return 1;
    }
    return n * Factorial(n - 1);
}


}  // namespace fact
