/*
 * 8_9_Quantization.cpp
 * Copyright (C) 2018 sungmin <smoh2044@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */


#include <bits/stdc++.h>


using namespace std;


int rec(vector<int>&v, int p, int s, vector<vector<int>>& memo){
    if(memo[p][s] < 0){
        int n = v.size();
        if(n-p <= s) return 0;
        if(s <= 0 && p < n) return INT_MAX;
        long long m = INT_MAX;
        for(int i=p+1; i<=n-s+1; ++i){
            int mid = round(accumulate(v.begin()+p, v.begin()+i, 0.0)/(i-p));
            long long rms = 0;
            for_each(v.begin()+p, v.begin()+i, [&](int& n){rms += pow(abs(n-mid), 2);});
            rms += rec(v, i, s-1, memo);
            if(rms < m){
                m = rms;
            }
        }
        if(m > INT_MAX){
            m = INT_MAX;
        }
        memo[p][s] = m;
    }
    return memo[p][s];
}

int solve(vector<int>& v, int s){
    sort(v.begin(), v.end());
    int n = v.size();
    vector<vector<int>> memo(n+1, vector<int>(s+1, -1));
    for(int i=0; i<n; ++i){
        for(int j=n-i; j<=s; ++j){
            memo[i][j] = 0;
        }
    }
    return rec(v, 0, s, memo);
}


int main(){
    int C;
    scanf("%d", &C);
    while(C--){
        int n, s;
        scanf("%d %d", &n, &s);
        vector<int> v(n);
        for(int i=0; i<n; ++i){
            scanf("%d", &v[i]);
        }
        printf("%d\n", solve(v, s));
    }

    return 0;
}
