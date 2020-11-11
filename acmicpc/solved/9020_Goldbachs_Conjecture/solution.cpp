#include <iostream>
#include <cstring>
#include <set>


using namespace std;

const int MAX = 10000;

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

    set<int> primeSet;
    for(int i=0; i<MAX; ++i){
        if(primes[i]) primeSet.insert(i);
    }

    int T, n;
    scanf("%d", &T);
    while(T--){
        scanf("%d", &n);
        int i = n/2;
        set<int>::iterator it;
        for(; i<=n; ++i){
            it = primeSet.find(i);
            if(it != primeSet.end()) break;
        }
        for(; it != primeSet.end(); ++it){
            if(primes[n - *it]){
                printf("%d %d\n", n-*it, *it);
                break;
            }
        }
    }

    return 0;
}
