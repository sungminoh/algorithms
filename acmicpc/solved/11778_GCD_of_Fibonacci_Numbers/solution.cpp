/*
 * solution.cpp
 * Copyright (C) 2017 Sungmin <smoh2044@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */

#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

/*
 * F(n) = F(n-2)+F(n-1) = 1F(n-3) + 2F(n-2) = 2F(n-4) + 3F(n-3) = 3F(n-5) + 5F(n-4)...
 * i.e. F(n) = F(k)F(n-(k+1)) + F(k+1)F(n-k)
 * F(n) = F(n-m)F(n-(n-m+1)) + F(n-m+1)F(n-(n-m)) = F(n-m)F(m-1) + F(n-m+1)F(m)
 * gcd(F(n), F(m)) = gcd(F(n)-kF(m), F(m)) = gcd(F(n-m)F(m-1), F(m))
 *
 * Lemma. gcd(F(k), F(k-1)) = 1
 * pf. gcd(F(1), F(2)) = gcd(1, 1) = 1
 *     assume that gcd(F(k), F(k-1)) = 1
 *     gcd(F(k+1), F(k)) = gcd(F(k)+F(k-1), F(k)) = gcd(F(k-1), F(k))
 *     by induction, qed.
 *
 * By Lemma, gcd(F(n-m)F(m-1), F(m)) = gcd(F(n-m), F(m))
 * Repeat same argument, gcd(F(n), F(m)) = gcd(F(s), F(1)) = F(s) where s = gcd(n, m)
 */


typedef unsigned long long LL;
const int MOD = 1000000007;
unordered_map<LL, int> F;

LL gcd(LL a, LL b){
    if(b > a){
        return gcd(b, a);
    }
    if(a % b == 0){
        return b;
    }
    return gcd(a%b, b);
}

int fibo(LL s){
    /*
     * F(a+b) = F(a-1)F(b) + F(a)F(b+1)
     * F(s/2, s-(s/2))
     */
    if(s == 0) return 0;
    else if(s <= 2) return 1;
    else if(s == 3) return 2;
    else{
        if(F.find(s) == F.end()){
            LL Fa1 = fibo(s/2 - 1)%MOD;
            LL Fb = fibo(s-(s/2))%MOD;
            LL Fa = fibo(s/2)%MOD;
            LL Fb1 = fibo(s-(s/2)+1)%MOD;
            F.insert(make_pair(s, ((Fa1*Fb)%MOD + (Fa*Fb1)%MOD)%MOD));
        }
        return F.at(s);
    }
}


int solve(LL n, LL m){
    LL g = gcd(n, m);
    int f = fibo(g);
    return f;
}

int main(){
    LL n, m;
    scanf("%llu %llu", &n, &m);
    printf("%d\n", solve(n, m));
    return 0;
}

