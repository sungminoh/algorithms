/*
 * solution.cpp
 * Copyright (C) 2017 Sungmin <smoh2044@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */

#include <iostream>
#include <set>

using namespace std;
typedef long long LL;

void buildDescendingNumbersOfLength(int n, bool digit[10], set<LL> &ret){
    //printf("buildDescendingNumbersOfLength(%d,", n);
    //for(int i=0; i<10; ++i) printf(" %d", digit[i]);
    //printf(",");
    //for(auto i : ret) printf(" %d", i);
    //printf(")\n");
    if(n == 0){
        LL num = 0;
        for(int i=9; i>=0; --i){
            if(!digit[i]) continue;
            num *= (LL) 10;
            num += (LL) i;
        }
        ret.insert(num);
        return;
    }
    for(int i=9; i>=0; --i){
        if(digit[i]) continue;
        digit[i] = true;
        buildDescendingNumbersOfLength(n-1, digit, ret);
        digit[i] = false;
    }
}

LL solve(int n){
    if(n > 1022) return -1;
    int comb[11] = {0, 10, 55, 175, 385, 637, 847, 967, 1012, 1022, 1023};
    int i;
    for(i=1; i<=10; ++i){
        if(n < comb[i]) break;
    }
    set<LL> numbers;
    bool digit[10] = {false};
    buildDescendingNumbersOfLength(i, digit, numbers);
    set<LL>::iterator it = numbers.begin();
    for(int j=comb[i-1]; j!=n && it!=numbers.end(); ++j,++it){
    }
    return *it;
}

int main(){
    /*
     * (10, 1) = 10
     * (10, 2) = 45
     * (10, 3) = 120
     * (10, 4) = 210
     * (10, 5) = 252
     * (10, 6) = 210
     * (10, 7) = 120
     * (10, 8) = 45
     * (10, 9) = 10
     * (10, 10) = 1
     */
    int n;
    scanf("%d", &n);
    printf("%lld\n", solve(n));

    return 0;
}
