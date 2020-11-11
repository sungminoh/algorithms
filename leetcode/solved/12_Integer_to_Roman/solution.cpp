/*
 * solution.cpp
 * Copyright (C) 2018 sungmin <smoh2044@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */

#include <iostream>
#include <vector>
#include <string>
#include <cmath>


using namespace std;


/*
Symbol	I	V	X	L	C	D	M
Value	1	5	10	50	100	500	1,000
*/


class Solution {
public:
    int scaleToIdx[4] = {0, 2, 4, 6};
    char digit[7] = {'I', 'V', 'X', 'L', 'C', 'D', 'M'};
    void adjust(int& num, vector<char>& ret, int scale){
        int base = pow(10, scale);
        if(num >= 9*base){
            ret.push_back(digit[scaleToIdx[scale]]);
            ret.push_back(digit[scaleToIdx[scale]+2]);
        }else if(num >= 5*base){
            ret.push_back(digit[scaleToIdx[scale]+1]);
            for(int i=num-(num%base)-(5*base); i>0; i-=base){
                ret.push_back(digit[scaleToIdx[scale]]);
            }
        }else if(num >= 4*base){
            ret.push_back(digit[scaleToIdx[scale]]);
            ret.push_back(digit[scaleToIdx[scale]+1]);
        }else if(num >= base){
            for(int i=num-(num%base); i>0; i-=base){
                ret.push_back(digit[scaleToIdx[scale]]);
            }
        }
        num %= base;
    }
    void intToRoman(int& num, vector<char>& ret){
        if(num == 0) return;
        if(num >= 1000){
            ret.push_back('M');
            num -= 1000;
        }else if(num >= 100){
            adjust(num, ret, 2);
        }else if(num >= 10){
            adjust(num, ret, 1);
        }else{
            adjust(num, ret, 0);
        }
        intToRoman(num, ret);
    }
    string intToRoman(int num) {
        vector<char> ret;
        intToRoman(num, ret);
        string s(ret.begin(), ret.end());
        return s;
    }
};


int main(){
    int n;
    cin >> n;
    cout << Solution().intToRoman(n) << endl;

    return 0;
}
