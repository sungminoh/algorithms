/*
 * solution.cpp
 * Copyright (C) 2018 sungmin <smoh2044@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */

#include <iostream>


using namespace std;


class Solution {
public:
    int divide(int dividend, int divisor) {
        if(divisor == 0) return INT_MAX;
        if(dividend == divisor) return 1;
        if(divisor == 1) return dividend;
        if(divisor == -1){
            if(dividend == INT_MIN) return INT_MAX;
            else return -dividend;
        }
        if(dividend < 0 && divisor > 0) return -divide(dividend, -divisor);
        if(dividend > 0 && divisor < 0) return -divide(-dividend, divisor);
        if(dividend > 0 && divisor > 0) return divide(-dividend, -divisor);
        int ret = 0;
        while(dividend <= divisor){
            long dvs = divisor, mul = 1;
            while(dividend <= (dvs << 1)){
                dvs <<= 1;
                mul <<= 1;
            }
            dividend -= dvs;
            ret += mul;
        }
        return ret;
    }
};


int main(){
    int a, b;
    cin >> a >> b;
    cout << Solution().divide(a, b) << endl;
    //cout << a/b << endl;

    return 0;
}
