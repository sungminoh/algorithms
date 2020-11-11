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

    //vector<bool> v(n+1, true);
    //v[0] = v[1] = false;
    //int i = 1;
    //while(i++ <= n/2){
        //if(!v[i]) continue;
        //for(int j=i+i; j<=n; j+=i){
            //v[j] = false;
        //}
    //}
    //return v;

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
    for(LL j=i; j<n; ++j){
        if(isPrime[j]){
            ret.push_back(j);
        }
    }
    return ret;
}

vector<LL> filterPrimeFactors(LL n, vector<LL> &primes){
    vector<LL> ret;
    for(auto prime : primes){
        if(n%prime != 0){
            ret.push_back(prime);
        }
    }
    return ret;
}

LL solve(LL n){
    vector<LL> primes = getPrimes(n);
    cout << "primes: ";
    for(auto prime : primes) cout << prime << ' ';
    cout << endl;
    vector<LL> relativelyPrimes = filterPrimeFactors(n, primes);
    cout << "relatively primes: ";
    for(auto prime : relativelyPrimes) cout << prime << ' ';
    cout << endl;
    vector<LL> heap;
    unordered_set<LL> visited;
    heap.push_back(-1);
    visited.insert(-1);
    make_heap(heap.begin(), heap.end());
    LL head = heap.front(); pop_heap(heap.begin(), heap.end()); heap.pop_back();
    LL cnt = 0;
    while(-head < n){
        //cout << "head " << -head << endl;
        cnt ++;
        for(auto prime : relativelyPrimes){
            LL n = head*prime;
            if(visited.find(n) != visited.end()) continue;
            visited.insert(n);
            heap.push_back(head*prime); push_heap(heap.begin(), heap.end());
        }
        head = heap.front(); pop_heap(heap.begin(), heap.end()); heap.pop_back();
    }
    return cnt;
}

int main(){
    LL n;
    scanf("%lld", &n);
    printf("%lld\n", solve(n));

    return 0;
}
