/*
 * solution.cpp
 * Copyright (C) 2018 sungmin <smoh2044@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */

#include <iostream>
#include <vector>
#include <string>
#include <sstream>


using namespace std;


class Solution {
public:
    int maxArea(vector<int>& height) {
        int m = 0, h = 0;
        int l = 0, r = height.size()-1;
        while(l<r){
            h = min(height[l], height[r]);
            m = max(m, h*(r-l));
            while(height[l] <= h && l < r) l++;
            while(height[r] <= h && l < r) r--;
        }
        return m;
    }
};


vector<int> getInputs(){
    string s;
    getline(cin, s);
    stringstream ss(s);

    vector<int> v;
    int n;
    while(ss >> n)
        v.push_back(n);
    return v;
}


int main(){
    vector<int> v = getInputs();
    cout << Solution().maxArea(v);
    return 0;
}
