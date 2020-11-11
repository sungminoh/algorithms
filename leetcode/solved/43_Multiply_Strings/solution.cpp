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
    string sum(string num1, string num2){
        stringstream ss;
        int i = num1.size()-1;
        int j = num2.size()-1;
        int c = 0;
        while(i>=0 || j>=0){
            int n1 = i >= 0 ? num1[i]-48 : 0;
            int n2 = j >= 0 ? num2[j]-48 : 0;
            c += n1+n2;
            ss << to_string(c%10);
            c = c/10;
            i--;
            j--;
        }
        if(c != 0) ss << to_string(c);
        string s = ss.str();
        reverse(s.begin(), s.end());
        return s;
    }
    string multiply(string num1, string num2) {
        if(num1.compare("0") == 0 || num2.compare("0") == 0) return "0";
        stringstream ss;
        string s = "0";
        int c = 0;
        int size1 = num1.size()-1;
        for(int i=size1; i>=0; --i){
            int n1 = num1[i]-48;
            for(int t=0; t<size1-i; ++t){
                ss << '0';
            }
            for(int j=num2.size()-1; j>=0; --j){
                int n2 = num2[j]-48;
                c += n1*n2;
                ss << to_string(c%10);
                c /= 10;
            }
            if(c != 0) ss << to_string(c);
            c = 0;
            string s2 = ss.str();
            reverse(s2.begin(), s2.end());
            s = sum(s, s2);
            ss.str("");
        }
        if(c != 0){
            s = to_string(c) + s;
        }
        return s;
    }
};



string input(){
    string s;
    getline(cin, s);
    return s;
}


int main(){
    string s1 = input();
    string s2 = input();
    cout << Solution().multiply(s1, s2) << endl;

    return 0;
}
