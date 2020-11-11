#include <iostream>

using namespace std;

int gcd(int a, int b){
    if(a < b){
        return gcd(b, a);
    }
    if(a%b == 0){
        return b;
    }
    return gcd(a%b, b);
}


int main(){
    int n, a, b;
    scanf("%d", &n);
    scanf("%d", &a);
    for(int i=1; i<n; ++i){
        scanf("%d", &b);
        printf("%d/%d\n", a/gcd(a, b), b/gcd(a, b));
    }
    return 0;
}
