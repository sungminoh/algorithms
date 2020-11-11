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
    int findUpperBound(vector<int>& nums, int target){
        int s, e, i, size;
        size = nums.size();
        s = 0, e = size-1;
        while(s<=e){
            i = s + (e-s)/2;
            if(nums[i] == target && (i==size-1 || nums[i+1] > target)) return i;
            if(nums[i] <= target) s = i+1;
            else e = i-1;
        }
        return -1;
    }

    int findLowerBound(vector<int>& nums, int target){
        int s, e, i, size;
        size = nums.size();
        s = 0, e = size-1;
        while(s<=e){
            i = s + (e-s)/2;
            if(nums[i] == target && (i==0 || nums[i-1] < target)) return i;
            if(nums[i] >= target) e = i-1;
            else s = i+1;
        }
        return -1;
    }

    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> ret;
        ret.push_back(findLowerBound(nums, target));
        ret.push_back(findUpperBound(nums, target));
        return ret;
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
    vector<int> sol = Solution().searchRange(v, t);
    for_each(sol.begin(), sol.end(), [](int i){cout << i << ' ';});

    return 0;
}
