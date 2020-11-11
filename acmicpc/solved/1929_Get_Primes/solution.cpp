#include <iostream>
#include <cstring>
#include <set>


using namespace std;

const int MAX = 1000001;

int main(){
    bool primes[MAX];
    memset(primes, true, sizeof(bool)*MAX);
    primes[1] = false;

    int M, N;
    scanf("%d %d", &M, &N);
    for(int i=2; i<=N; ++i){
        if(primes[i] == false) continue;
        for(int j=i*2; j<MAX; j+=i){
            primes[j] = false;
        }
    }

    for(int i=M; i<=N; i++){
        if(primes[i])
            printf("%d\n", i);
    }

    return 0;
}
