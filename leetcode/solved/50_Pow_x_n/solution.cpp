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
    double myPow(double x, int n) {
        if(x == 0){
            return 0;
        }else if(n == 0 || x == 1.){
            return 1.;
        }else if(n == 1){
            return x;
        }else if(n < 0){
            return (1./x) * myPow(1./x, -(n+1));
        }else{
            int d = n/2;
            int r = n%2;
            double v = myPow(x, d);
            return v * v * (r == 1 ? x : 1);
        }
    }
};


int main(){
    int x, n;
    scanf("%d %d", &x, &n);
    cout << Solution().myPow(x, n) << endl;

    return 0;
}
