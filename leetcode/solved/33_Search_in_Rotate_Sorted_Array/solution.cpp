/*
 * solution.cpp
 * Copyright (C) 2018 sungmin <smoh2044@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */


#include <bits/stdc++.h>


using namespace std;


class Solution {
public:
    int bisearch(vector<int>& v, int s, int e, int t){
        if(s >= e) return -1;
        int i = s + (e-s)/2;
        if(v[i] == t) return i;
        int ret = -1;
        if(t < v[i]){
            ret = bisearch(v, s, i, t);
            if(ret < 0) ret = bisearch(v, i+1, e, t);
        }else{
            ret = bisearch(v, i+1, e, t);
            if(ret < 0) ret = bisearch(v, s, i, t);
        }
        if(ret >= 0) return ret;
        return -1;
    }

    int findPivot(vector<int>& v){
        int s = 0;
        int e = v.size()-1;
        int i;
        while(s < e){
            i = s + (e-s)/2;
            if(v[i] > v[e]) s = i+1;
            else e = i;
        }
        return s;
    }

    int search(vector<int>& nums, int target) {
        //return bisearch(nums, 0, nums.size(), target);
        int size = nums.size();
        int p = findPivot(nums);
        int s = 0;
        int e = size-1;
        int i_, i;
        while(s<=e){
            i_ = s + (e-s)/2;
            i = (i_ + p) % size;
            if(nums[i] == target) return i;
            if(nums[i] > target) e = i_-1;
            else s = i_+1;
        }
        return -1;
    }
};

vector<int> getInput(){
    string s;
    getline(cin, s);
    stringstream ss(s);
    vector<int> ret;
    int n;
    while(ss >> n)
        ret.push_back(n);
    return ret;
}


int main(){
    vector<int> v = getInput();
    int t;
    cin >> t;
    cout << Solution().search(v, t) << endl;

    return 0;
}
