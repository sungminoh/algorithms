/*
 * solution.cpp
 * Copyright (C) 2017 Sungmin <smoh2044@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */

#include <iostream>
#include <vector>
#include <cmath>
#include <unordered_set>

using namespace std;

typedef long long LL;
const LL MAX = 1000000000001;


void printVector(const vector<int> &v){
    for (const auto& i : v)
        cout << i << ' ';
}


vector<bool> findPrimes(int n){
    vector<bool> v(n+1, true);
    v[0] = v[1] = false;
    int i = 1;
    while(i++ <= n/2){
        if(!v[i]) continue;
        for(int j=i+i; j<=n; j+=i){
            v[j] = false;
        }
    }
    return v;
}


LL solve(LL m, LL n){
    vector<bool> candidates(n-m+1, true);
    int primeMax = floor(sqrt(n+1));
    //cout << "primeMax: " << primeMax << endl;
    vector<bool> primes = findPrimes(primeMax);

    LL ret = 0;
    for(int i=2; i<=primeMax; ++i){
        if(!primes[i]) continue;
        LL iSquare = (long long) i * i;
        LL firstMet = m % iSquare == 0 ? m : (m + iSquare) - (m % iSquare);
        //cout << "Prime: " << i << " Square: " << iSquare << endl;
        //cout << "firstMet: " << firstMet << endl;
        for(LL j=firstMet; j<=n; j+=iSquare){
            if(candidates[j-m]){
                //cout << j << " is divided by " << iSquare << " (" << i << ")"<< endl;
                ret += 1;
                candidates[j-m] = false;
            }
        }
    }
    return (n-m+1)-ret;
}


int main(){
    ios_base::sync_with_stdio(false);
    LL m, n;
    cin >> m >> n;
    int ret = solve(m, n);
    cout << ret << endl;
    return 0;
}
