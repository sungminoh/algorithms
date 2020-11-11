#include <iostream>
#include <set>

using namespace std;


set<int> primes;

bool isPrime(int n){
    //for(set<int>::iterator prime=primes.begin(); prime!=primes.end(); ++prime){
    for(auto& prime : primes){
        if(n % prime == 0)
            return false;
    }
    return true;
}

int main(){
    int N, n, cnt=0;

    for(int i=2; i<=1000; ++i){
        if(isPrime(i)){
            primes.insert(i);
        }
    }

    //for(auto& prime : primes){
        //printf("%d\t", prime);
    //}

    scanf("%d", &N);
    for(int i=0; i<N; ++i){
        scanf("%d", &n);
        if(primes.find(n) != primes.end()) cnt++;
    }

    cout << cnt;

    return 0;
}
