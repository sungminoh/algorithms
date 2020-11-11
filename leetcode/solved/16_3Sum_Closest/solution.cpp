/*
 * solution.cpp
 * Copyright (C) 2018 sungmin <smoh2044@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */

#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <cmath>


using namespace std;


class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int size = nums.size();
        int ret = nums[0]+nums[1]+nums[2];
        for(int i=0; i<size; ++i){
            int l = i+1;
            int r = size-1;
            while(l < r){
                int s = nums[l] + nums[r] + nums[i];
                if(abs(s-target) < abs(ret-target)){
                    ret = s;
                }
                if(s > target){
                    r--;
                }else if(s < target){
                    l++;
                }else{
                    return target;
                }
            }
        }
        return ret;
    }
};


pair<int, vector<int>> getInput(){
    string s;
    getline(cin, s);
    stringstream ss(s);
    int target;
    ss >> target;
    vector<int> lst;
    int n;
    while(ss >> n)
        lst.push_back(n);
    return {target, lst};
}


int main(){
    pair<int, vector<int>> i = getInput();
    cout << Solution().threeSumClosest(i.second, i.first) << endl;

    return 0;
}
