/*
 * solution.cpp
 * Copyright (C) 2018 sungmin <smoh2044@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */

#include <iostream>
#include <vector>
#include <set>
#include <algorithm>


using namespace std;


class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> ret;
        if(n == 0){
            ret.push_back("");
            return ret;
        }
        if(n == 1){
            ret.push_back("()");
            return ret;
        }
        for(int i=0; i<n; ++i){
            for(auto l: generateParenthesis(i)){
                for(auto r: generateParenthesis(n-i-1)){
                    ret.push_back(l + "(" + r + ")");
                }
            }
        }
        return ret;
    }
};


int main(){
    int n;
    cin >> n;
    vector<string> ret = Solution().generateParenthesis(n);
    for(auto s : ret){
        cout << s << endl;
    }

    return 0;
}
