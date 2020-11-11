/*
 * solution.cpp
 * Copyright (C) 2018 sungmin <smoh2044@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */

#include <iostream>
#include <vector>
#include <cstdlib>


using namespace std;


class Solution {
public:
    string strings[10] = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
    vector<string> letterCombinations(string digits) {
        vector<string> ret;
        int size = digits.size();
        if(size == 0){
            return ret;
        }
        if(size == 1){
            string s = strings[digits[0]-48];
            for(auto c : s){
                ret.push_back(string(1, c));
            }
            return ret;
        }
        vector<string> sub = letterCombinations(digits.substr(1, size));
        for(char c : strings[digits[0]-48]){
            for(string s : sub){
                ret.push_back(c + s);
            }
        }
        return ret;
    }
};


int main(){
    string digits;
    getline(cin, digits);
    vector<string> sol = Solution().letterCombinations(digits);
    for_each(sol.begin(), sol.end(), [](string& s){cout << s << " ";});

    return 0;
}
