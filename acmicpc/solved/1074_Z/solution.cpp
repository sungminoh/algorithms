/*
 * solution.cpp
 * Copyright (C) 2017 Sungmin <smoh2044@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */

#include <iostream>
#include <cmath>

using namespace std;

int getOrder(int n, int r, int c){
    if(n == 0){
        return 0;
    }
    int m = n/2;
    if(r <= m && c <= m){
        return getOrder(m, r, c);
    }else if(r <= m && c > m){
        return m*m + getOrder(m, r, c-m);
    }else if(r > m && c <= m){
        return 2*m*m + getOrder(m, r-m, c);
    }else{
        return 3*m*m + getOrder(m, r-m, c-m);
    }
}


int main(){
    int n, r, c;
    scanf("%d %d %d", &n, &r, &c);
    printf("%d\n", getOrder(pow(2, n), r+1, c+1));

    return 0;
}
