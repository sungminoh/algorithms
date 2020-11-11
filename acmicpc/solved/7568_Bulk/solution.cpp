/*
 * solution.cpp
 * Copyright (C) 2017 Sungmin <smoh2044@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */

#include <iostream>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

bool cmp(const pair<int, int> &a, const pair<int, int> &b){
    return a.first > b.first && a.second > b.second;
}

int main(){
    int n;
    scanf("%d", &n);

    vector<pair<int, int> > lst(n);
    for(int i=0; i<n; ++i){
        int w, h;
        scanf("%d %d", &w, &h);
        pair<int, int> s = make_pair(w, h);
        lst[i] = s;
    }

    vector<int> ranking(n, 1);
    for(int i=0; i<n; ++i){
        for(int j=i+1; j<n; j++){
            if(cmp(lst[i], lst[j])){
                ranking[j] += 1;
            }else if(cmp(lst[j], lst[i])){
                ranking[i] += 1;
            }
        }
    }

    for(auto r : ranking) printf("%d ", r);

    return 0;
}
