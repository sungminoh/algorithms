#include <iostream>
#include <set>


using namespace std;


set<int> getPrimes(int n){
    set<int> primes;

    for(int i=2; i<=n; ++i){
        bool found = true;
        for(auto& prime : primes){
            if(i % prime == 0){
                found = false;
            }
        }
        if(found)
            primes.insert(i);
    }

    return primes;
}

int main(){
    int M, N, sum=0, m=-1;

    scanf("%d", &M);
    scanf("%d", &N);

    set<int> primes = getPrimes(N);

    //for(auto& prime : primes){
        //printf("%d\t", prime);
    //}
    //printf("\n");

    for(auto& prime : primes){
        if(prime < M) continue;
        if(m == -1) m = prime;
        sum += prime;
    }

    if(sum){
        printf("%d\n%d\n", sum, m);
    }else{
        printf("%d\n", -1);
    }
    //cout << sum << endl << m << endl;

    return 0;
}
