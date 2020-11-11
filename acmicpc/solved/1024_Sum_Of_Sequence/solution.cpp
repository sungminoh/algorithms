/*
 * solution.cpp
 * Copyright (C) 2017 Sungmin <smoh2044@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */

#include <iostream>
#include <math.h>

using namespace std;


pair<int, int> getNumberOfTwoAndOdd(int l){
    int cnt = 0;
    while(l % 2 == 0){
        cnt++;
        l /= 2;
    }
    return make_pair(cnt, l);
}

bool isSuccess(int n, int numberOfTwo, int odd){
    //printf("\nn: %d\ntwo: %d\nodd: %d\n", n, numberOfTwo, odd);

    if(odd != 1){
        return n % odd == 0 ? isSuccess(n/odd, numberOfTwo, 1) : false;
    }

    if(numberOfTwo > 1){
        return n % 2 == 0 ? isSuccess(n/2, numberOfTwo - 1, 1) : false;
    }

    return numberOfTwo == 0 || n % 2 != 0 ? true : false;
}


int main(){
    int n, l;
    scanf("%d %d", &n, &l);

    pair<int, int> numberOfTwoAndOdd = getNumberOfTwoAndOdd(l);
    int numberOfTwo = numberOfTwoAndOdd.first;
    int odd = numberOfTwoAndOdd.second;

    // find minimum l
    while(l <= 100 && !isSuccess(n, numberOfTwo, odd)){
        l++;
        numberOfTwoAndOdd = getNumberOfTwoAndOdd(l);
        numberOfTwo = numberOfTwoAndOdd.first;
        odd = numberOfTwoAndOdd.second;
    }

    if(l > 100){
        printf("%d\n", -1);
    }else{
        //printf("l: %d\n", l);
        int start = n/l - (l-1)/2;
        if(start < 0){
            printf("%d\n", -1);
        }else{
            for(int i=0; i<l; i++){
                printf("%d ", start + i);
            }
            printf("\n");
        }
    }

    return 0;
}
