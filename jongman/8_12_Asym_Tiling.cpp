/*
 * 8_12_Asym_Tiling.cpp
 * Copyright (C) 2018 sungmin <smoh2044@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */


#include <bits/stdc++.h>


using namespace std;

int MOD = 1000000007;


int tiling(int n, vector<int>& memo){
    int& ret = memo[n];
    if(ret >= 0) return ret;
    return ret = (tiling(n-1, memo) + tiling(n-2, memo)) % MOD;
}


int asymTiling(int n, vector<int>& memo){
    if(n % 2 == 1){
        return (tiling(n, memo) - tiling(n/2, memo) + MOD) % MOD;
    }
    int ret = tiling(n, memo);
    ret = (ret - tiling(n/2, memo) + MOD) % MOD;
    ret = (ret - tiling(n/2 -1, memo) + MOD) % MOD;
    return ret;
}

int main(){
    ios_base::sync_with_stdio(false);
    int C, n;
    cin >> C;
    while(C--){
        cin >> n;
        vector<int> memo(n+1, -1);
        memo[0] = 1;
        memo[1] = 1;
        memo[2] = 2;
        cout << asymTiling(n, memo);
    }
    return 0;
}
