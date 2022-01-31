/*
 * solution.cpp
 * Copyright (C) 2018 sungmin <smoh2044@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */

#include <iostream>
#include <string>


using namespace std;


class Solution {
public:
    static inline void  ltrim(string &s) {
        s.erase(s.begin(), find_if(s.begin(), s.end(), [](int ch) {return !isspace(ch);}));
    }
    static inline void  rtrim(string &s) {
        s.erase(find_if(s.rbegin(), s.rend(), [](int ch) {return !isspace(ch);}).base(), s.end());
    }
    static inline bool isNumber(char &c) {
        return c >= 48 && c <= 57;
    }
    static inline int getSign(string &s) {
        if(s[0] == '-'){
            s.erase(s.begin(), s.begin() + 1);
            return -1;
        }else if(s[0] == '+'){
            s.erase(s.begin(), s.begin() + 1);
        }
        return 1;
    }
    int myAtoi(string str) {
        ltrim(str);
        rtrim(str);
        int neg = getSign(str);
        if(str.length() == 0){
            return 0;
        }
        long ret = 0;
        long scale = 1;
        bool overflow = false;
        for(auto it = str.rbegin(); it != str.rend(); ++it) {
            if(!isNumber(*it)){
                ret = 0;
                scale = 1;
                continue;
            }
            if(!overflow) ret += (*it - 48) * scale * neg;
            if(ret > INT_MAX){
                ret = INT_MAX;
                overflow = true;
            }else if(ret < INT_MIN){
                ret = INT_MIN;
                overflow = true;
            }
            scale *= 10;
        }
        return (int) ret;
    }
};


int main(){
    string str;
    getline(cin, str);
    cout << Solution().myAtoi(str);

    return 0;
}
