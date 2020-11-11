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

void printVec(vector<int>& v){
    cout << "[" << join(v, ", ") << "]" << endl;
}

class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> ret;
        if(target < 0){
            return ret;
        }
        if(target == 0){
            vector<int> v;
            ret.push_back(v);
            return ret;
        }
        int size = candidates.size();
        for(int i=0; i<size; ++i){
            int n = candidates[i];
            for(int t=target-n; t>=0; t-=n){
                vector<int> c(candidates.begin()+1+i, candidates.end());
                for(auto v : combinationSum(c, t)){
                    for(int j=(target-t)/n; j>0; --j){
                        v.push_back(n);
                    }
                    ret.push_back(v);
                }
            }
        }
        return ret;
    }
};


vector<int> getInput(){
    string s;
    getline(cin , s);
    stringstream ss(s);
    vector<int> ret;
    int n;
    while(ss >> n)
        ret.push_back(n);
    return ret;
}


int main(){
    vector<int> v = getInput();
    int n;
    cin >> n;
    vector<vector<int>> sols = Solution().combinationSum(v, n);
    for(auto sol : sols){
        printVec(sol);
    }

    return 0;
}
