/*
 * solution.cpp
 * Copyright (C) 2018 sungmin <smoh2044@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */

#include <iostream>
#include <vector>
#include <sstream>
#include <algorithm>


using namespace std;


class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int size = nums.size();
        for(int i=size-2; i>=0; --i){
            int idx = i;
            int target = INT_MAX;
            for(int j=i+1; j<size; ++j){
                if(nums[i] < nums[j] && nums[j] < target){
                    target = nums[j];
                    idx = j;
                }
            }
            if(target < INT_MAX){
                int tmp = nums[idx];
                nums[idx] = nums[i];
                nums[i] = tmp;
                sort(nums.begin()+i+1, nums.end());
                return;
            }
        }
        sort(nums.begin(), nums.end());
    }
};



vector<int> getInput(){
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
    vector<int> nums = getInput();
    Solution().nextPermutation(nums);
    for(auto it=nums.begin(); it!=nums.end(); ++it)
        cout << *it << " ";
    cout << endl;

    return 0;
}
