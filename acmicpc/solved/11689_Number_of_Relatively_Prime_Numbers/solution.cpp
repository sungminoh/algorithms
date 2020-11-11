/*
 * solution.cpp
 * Copyright (C) 2017 Sungmin <smoh2044@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */

#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <unordered_set>

using namespace std;

typedef long long LL;

vector<LL> getPrimes(LL n){
    vector<bool> isPrime(n+1, true);
    isPrime[0] = isPrime[1] = false;
    vector<LL> ret;
    LL i = 0;
    while(++i <= n/2){
        if(!isPrime[i]) continue;
        ret.push_back(i);
        for(LL j=i+i; j<=n; j+=i){
            isPrime[j] = false;
        }
    }
    for(LL j=i; j<=n; ++j){
        if(isPrime[j]){
            ret.push_back(j);
        }
    }
    return ret;
}

vector<pair<LL, LL> > getPrimeFactors(LL n, vector<LL> &primes){
    vector<pair<LL, LL> > ret;
    for(auto prime : primes){
        LL cnt = 0;
        while(n % prime == 0){
            n /= prime;
            cnt ++;
        }
        if(cnt > 0){
            ret.push_back(make_pair(prime, cnt));
        }
    }
    if(n > 1) ret.push_back(make_pair(n, 1));
    return ret;
}

LL solve(LL n){
    if(n == 1) return 1;
    vector<LL> primes = getPrimes(floor(sqrt(n)));
    vector<pair<LL, LL> > primeFactors = getPrimeFactors(n, primes);
    LL cnt = n;
    /* [Euler's phi function](https://ko.wikipedia.org/wiki/%EC%98%A4%EC%9D%BC%EB%9F%AC_%ED%94%BC_%ED%95%A8%EC%88%98)*/
    for(auto prime_cnt : primeFactors){
        LL p = prime_cnt.first;
        cnt -= cnt/p;
    }
    return cnt;
}

int main(){
    LL n;
    scanf("%lld", &n);
    printf("%lld\n", solve(n));

    return 0;
}
