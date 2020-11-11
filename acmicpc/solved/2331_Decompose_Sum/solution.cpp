/*
 * solution.cpp
 * Copyright (C) 2017 Sungmin <smoh2044@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */

#include <iostream>

using namespace std;


int getDigitSum(int n){
    int ret = 0;
    while(n){
        ret += n%10;
        n /= 10;
    }
    return ret;
}


int gen(int n){
    for(int i=1; i<n; ++i){
        if(i + getDigitSum(i) == n) return i;
    }
    return 0;
}


int main(){
    int n;
    scanf("%d", &n);
    printf("%d\n", gen(n));

    return 0;
}
