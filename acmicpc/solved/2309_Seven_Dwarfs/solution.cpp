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

vector<int> getInput(int n){
    vector<int> ret(n);
    for(int i=0; i<n; ++i){
        scanf("%d", &ret[i]);
    }
    return ret;
}


bool buildSubsetOfSum(vector<int> &v, int i, int j, int s, set<int> &ret){
    if(i == j){
        if(s == 0 && ret.size() == 7) return true;
        else return false;
    };
    ret.insert(v[i]);
    if(buildSubsetOfSum(v, i+1, j, s-v[i], ret)) return true;
    ret.erase(v[i]);
    if(buildSubsetOfSum(v, i+1, j, s, ret)) return true;
    return false;
}


int main(){
    vector<int> heights = getInput(9);
    set<int> s;
    if(buildSubsetOfSum(heights, 0, heights.size(), 100, s)){
        for(auto h : s){
            printf("%d\n", h);
        }
    }
    return 0;
}
