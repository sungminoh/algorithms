/*
 * 8_12_LIS.cpp
 * Copyright (C) 2017 Sungmin <smoh2044@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int lis_(vector<int>& s, vector<int>& cache, int start){
    int& ret = cache[start+1];
    if(ret > 0) return ret;
    ret = 1;
    int n = s.size();
    for(int i=start+1; i<n; ++i){
        if(start == -1 || s[start] < s[i]){
            ret = max(ret, lis_(s, cache, i) + 1);
        }
    }
    return ret;
}

int lis(vector<int>& s){
    vector<int> cache(s.size(), -1);
    return lis_(s, cache, -1) - 1;
}

int lis2(vector<int>& s){
    vector<int> c;
    int n = s.size();
    for(int i=0; i<n; ++i){
        int l = c.size();
        for(auto it=upper_bound(c.begin(), c.end(), s[i]); it!=c.end(); ++it){
            if((it == c.begin() || *(it - 1) < s[i]) && *it > s[i]) *it = s[i];
        }
        if(l == 0 || c[l-1] < s[i]) c.push_back(s[i]);
    }
    return c.size();
}

const long long NEGINF = numeric_limits<long long>::min();

int jlis_(vector<int>& a, vector<int>& b, int i, int j, vector<vector<int> >& cache){
    int& ret = cache[i+1][j+1];
    if(ret > 0) return ret;
    ret = 2;

    long long ai = (i == -1 ? NEGINF : a[i]);
    long long bj = (j == -1 ? NEGINF : b[j]);
    int n = a.size(), m = b.size(), c = max(ai, bj);

    for(int i_=i+1; i_<n; ++i_){
        if(c < a[i_]){
            ret = max(ret, jlis_(a, b, i_, j, cache) + 1);
        }
    }
    for(int j_=j+1; j_<m; ++j_){
        if(c < b[j_]){
            ret = max(ret, jlis_(a, b, i, j_, cache) + 1);
        }
    }
    return ret;
}

int jlis(vector<int>& a, vector<int>& b){
    int n = a.size(), m = b.size();
    vector<vector<int> > cache(n+1, vector<int>(m+1, -1));
    return jlis_(a, b, -1, -1, cache) - 2;
}

int main(){
    int c;
    scanf("%d", &c);
    while(c--){
        int n, m;
        scanf("%d %d", &n, &m);

        vector<int> a(n);
        for(int i=0; i<n; i++){
            scanf("%d", &a[i]);
        }

        vector<int> b(m);
        for(int i=0; i<m; i++){
            scanf("%d", &b[i]);
        }

        printf("%d\n", jlis(a, b));
    }

    return 0;
}
