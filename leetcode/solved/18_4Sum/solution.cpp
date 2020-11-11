/*
 * solution.cpp
 * Copyright (C) 2018 sungmin <smoh2044@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */

#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <set>


using namespace std;


class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> ret;
        int size = nums.size();
        for(int i=0; i<size; ++i){
            for(int j=i+1; j<size; ++j){
                int l = j+1, r = size-1;
                while(l < r){
                    int sum = nums[i] + nums[j] + nums[l] + nums[r];
                    if(sum > target){
                        r--;
                    }else if(sum < target){
                        l++;
                    }else{
                        int sol[4] = {nums[i], nums[j], nums[l], nums[r]};
                        vector<int> result(sol, sol + sizeof(sol) / sizeof(int));
                        ret.push_back(result);
                        while(l < r && nums[l] == sol[2]) l++;
                        while(l < r && nums[r] == sol[3]) r--;
                    }
                }
                while(j+1 < size && nums[j] == nums[j+1]) j++;
            }
            while(i+1 < size && nums[i] == nums[i+1]) i++;
        }
        return ret;
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
    vector<int> v = getInput();
    int target = 0;
    cin >> target;
    vector<vector<int>> ret = Solution().fourSum(v, target);
    for_each(ret.begin(), ret.end(), [](vector<int>& r){
            for_each(r.begin(), r.end(), [](int n){cout << n << " ";});
            cout << endl;
            });

    return 0;
}
