/*
 * solution.cpp
 * Copyright (C) 2018 sungmin <smoh2044@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */


#include <bits/stdc++.h>


using namespace std;


string join(vector<int>& v, string delim){
    stringstream ss;
    for_each(v.begin(), v.end()-1, [&](int x){ss << to_string(x) << delim;});
    ss << *v.rbegin();
    return ss.str();
}


class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> ret;
        return permute(nums);
    }

    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> ret;
        int size = nums.size();
        if(size == 0) return vector<vector<int>>(1, vector<int>());
        for(int i=0; i<size; ++i){
            int n = nums[i];
            nums.erase(nums.begin() + i);
            vector<vector<int>> sub = permute(nums);
            for(auto v: sub){
                v.push_back(n);
                ret.push_back(v);
            }
            nums.insert(nums.begin() + i, n);
            while(i<size-1 && nums[i+1]==n) ++i;
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
    vector<vector<int>> ans = Solution().permuteUnique(v);
    for(auto v: ans){
        cout << join(v, " ") << endl;
    }

    return 0;
}

