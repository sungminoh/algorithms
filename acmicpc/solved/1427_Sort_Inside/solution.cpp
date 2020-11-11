#include <iostream>
#include <cstring>

using namespace std;

int main(){
    int n, bin[10];
    memset(bin, 0, sizeof(int) * 10);

    for(scanf("%d", &n); n; n/=10){
        bin[n%10] ++;
    }

    //for(int i=0; i<10; ++i){
        //printf("%d\t", bin[i]);
    //}

    int ans = 0, decimal = 1;
    for(int i=0; i<10; ++i){
        while(bin[i]--){
            ans += i * decimal;
            decimal *= 10;
        }
    }

    cout << ans;

    return 0;
}
