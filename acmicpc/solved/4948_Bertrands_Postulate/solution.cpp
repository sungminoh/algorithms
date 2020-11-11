#include <iostream>
#include <cstring>


using namespace std;

const int MAX = 123456*2 + 5;

int main(){
    bool primes[MAX];
    memset(primes, true, sizeof(bool)*MAX);
    primes[1] = false;

    for(int i=2; i<=MAX; ++i){
        if(primes[i] == false) continue;
        for(int j=i*2; j<MAX; j+=i){
            primes[j] = false;
        }
    }

    int n;
    while(true){
        scanf("%d", &n);
        if(n == 0) break;
        int cnt = 0;
        for(int i=n+1; i<=n*2; ++i){
            if(primes[i]) cnt++;
        }
        printf("%d\n", cnt);
    }

    return 0;
}
