#include <iostream>

using namespace std;

typedef long long LL;

LL gcd(LL a, LL b){
    if(b > a){
        return gcd(b, a);
    }
    if(a % b == 0){
        return b;
    }
    return gcd(a%b, b);
}

LL lcm(LL a, LL b){
    LL c = gcd(a, b);
    return a * b / c;
}

int main(){
    LL a, b;
    scanf("%lld %lld", &a, &b);
    printf("%lld\n", lcm(a, b));
    return 0;
}
