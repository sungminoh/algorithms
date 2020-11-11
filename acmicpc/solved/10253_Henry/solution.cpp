/*
 * solution.cpp
 * Copyright (C) 2017 Sungmin <smoh2044@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */

#include <iostream>
#include <cmath>

using namespace std;


int gcd(int a, int b){
    if(a < b){
        return gcd(b, a);
    }
    if(a % b == 0){
        return b;
    }
    return gcd(a % b, b);
}

pair<int, int> subtract(int a1, int b1, int a2, int b2){
    int b = b1 * b2;
    int a = (a1 * b2) - (a2 * b1);

    int g = gcd(a, b);
    return make_pair(a / g, b / g);
}


int getHenry(int a, int b){
    if(a == 1){
        return b;
    }

    int g = gcd(a, b);
    if(g > 1){
        return getHenry(a / g, b / g);
    }

    int a_ = 1;
    int b_ = ceil((double) b / a);

    pair<int, int> ab = subtract(a, b, a_, b_);
    return getHenry(ab.first, ab.second);
}


int main(){
    int t, a, b;
    scanf("%d", &t);
    while(t--){
        scanf("%d %d", &a, &b);
        int henry = getHenry(a, b);
        printf("%d\n", henry);
    }

    return 0;
}
