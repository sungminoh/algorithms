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
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> ret;
        int size = nums.size();
        for(int i=0; i<size; ++i){
            int target = -nums[i];
            int l = i+1, r = size-1;
            while(l < r){
                int sum = nums[l] + nums[r];
                if(sum > target){
                    r--;
                }else if(sum < target){
                    l++;
                }else{
                    int sol[3] = {nums[i], nums[l], nums[r]};
                    vector<int> result(sol, sol + sizeof(sol) / sizeof(int));
                    ret.push_back(result);
                    while(l < r && nums[l] == sol[1]) l++;
                    while(l < r && nums[r] == sol[2]) r--;
                }
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
    vector<vector<int>> ret = Solution().threeSum(v);
    for_each(ret.begin(), ret.end(), [](vector<int>& r){
            for_each(r.begin(), r.end(), [](int n){cout << n << " ";});
            cout << endl;
            });

    return 0;
}
