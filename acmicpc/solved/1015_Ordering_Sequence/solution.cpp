/*
 * solution.cpp
 * Copyright (C) 2017 Sungmin <smoh2044@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */

#include <iostream>
#include <vector>
#include <set>

using namespace std;

vector<int> getInput(){
    int n;
    cin >> n;
    vector<int> v(n);
    for(int i=0; i<n; ++i)
        cin >> v[i];
    return v;
}

vector<int> solve(vector<int> &v){
    vector<set<int> > tmp(1001, set<int>());
    int n = v.size();
    for(int i=0; i<n; ++i){
        tmp[v[i]].insert(i);
    }
    vector<int> ret(n);
    int i = 0;
    for(int j=1; j<=1000; ++j){
        for(auto x : tmp[j]){
            ret[x] = i++;
        }
    }
    return ret;
}


int main(){
    ios_base::sync_with_stdio(false);
    vector<int> v = getInput();
    vector<int> r = solve(v);
    for(auto x : r)
        cout << x << ' ';
    cout << endl;
    return 0;
}
