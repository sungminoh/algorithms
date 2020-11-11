/*
 * 8_14_Poly.cpp
 * Copyright (C) 2018 sungmin <smoh2044@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */


#include <bits/stdc++.h>


using namespace std;


int MOD =  10000000;

int poly(int n, int h, vector<vector<int>>& memo){
    if(n == h) return 1;
    int& ret = memo[n][h];
    if(ret >= 0) return ret;
    ret = 0;
    for(int i=1; i<=n-h; ++i){
        ret += (poly(n-h, i, memo) * (i+h-1)) % MOD;
        ret %= MOD;
    }
    return ret;
}


int main(){
    ios_base::sync_with_stdio(false);
    int C, n;
    cin >> C;
    while(C--){
        cin >> n;
        vector<vector<int>> memo(n+1, vector<int>(n+1, -1));
        int ret = 0;
        for(int i=1; i<=n; ++i){
            ret += poly(n, i, memo);
        }
        cout << ret;
    }

    return 0;
}
