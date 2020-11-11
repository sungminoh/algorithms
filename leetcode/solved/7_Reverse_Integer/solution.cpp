/*
 * solution.cpp
 * Copyright (C) 2018 sungmin <smoh2044@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */

#include <iostream>


using namespace std;


int reverse(int x) {
    if(x == 0){
        return 0;
    }
    int neg = 1;
    if(x < 0){
        neg = -1;
        x *= -1;
    }
    long i = 1;
    for(; i <= x; i *= 10){}
    i /= 10;
    long ret = 0;
    for(; i > 0; i /= 10, x /= 10){
        ret += (i * (x%10));
        if(ret > INT_MAX){
            return 0;
        }
    }
    return neg * ret;
}


int main(){
    int x;
    scanf("%d", &x);
    int y = reverse(x);
    printf("%d\n", y);
    return 0;
}
