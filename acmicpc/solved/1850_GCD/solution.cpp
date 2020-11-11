#include <iostream>
#include <vector>
#include <string>

using namespace std;

typedef unsigned long long LL;


LL gcd(LL a, LL b){
    if(b > a){
        return gcd(b, a);
    }
    if(a % b == 0){
        return b;
    }
    return gcd(a%b, b);
}

int main(){
    LL a, b;
    scanf("%llu %llu", &a, &b);
    LL c = gcd(a, b);
    string s(c, '1');
    cout << s;
    return 0;
}
