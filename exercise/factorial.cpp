#include <iostream>

typedef unsigned long long LL;

using namespace std;

LL factorial(int n){
    if(n <= 1){
        return 1;
    }
    return n * factorial(n - 1);
}

int main(){
    int n;
    scanf("%d", &n);
    LL ans = factorial(n);
    printf("%llu\n", ans);

    return 0;
}
