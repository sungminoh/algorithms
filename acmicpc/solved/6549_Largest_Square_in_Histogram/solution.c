/*
 * solution.c
 * Copyright (C) 2017 Sungmin <smoh2044@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */

#include "stdio.h"


int hist[100000];

long long int getMaxSize(int s, int e){
    if(e < s){
        return -1;
    }
    if(s == e){
        /*printf("[%d, %d]: %d\n", s, e, hist[s]);*/
        return hist[s];
    }
    int mid = (s + e) / 2;
    long long int leftSize = getMaxSize(s, mid-1);
    long long int rightSize = getMaxSize(mid+1, e);

    int i = mid-1;
    int j = mid+1;
    int h = hist[mid];
    long long int size = hist[mid];
    while(s <= i || j <= e){
        /*printf("(%d, %d): %lld\n", i, j, size);*/
        long long int _size;
        int leftHeight, rightHeight;
        if(i < s){
            h = hist[j] < h ? hist[j] : h;
            _size = (long long int) h * (j - i);
            size = size < _size ? _size : size;
            j++;
            continue;
        }else{
            leftHeight = hist[i] < h ? hist[i] : h;
        }

        if(j > e){
            h = leftHeight;
            _size = (long long int) h * (j - i);
            size = size < _size ? _size : size;
            i--;
            continue;
        }else{
            rightHeight = hist[j] < h ? hist[j] : h;
            if(leftHeight < rightHeight){
                h = rightHeight;
                _size = (long long int) h * (j - i);
                size = size < _size ? _size : size;
                j++;
            }else{
                h = leftHeight;
                _size = (long long int) h * (j - i);
                size = size < _size ? _size : size;
                i--;
            }
        }
    }

    /*printf("[%d, %d]: %lld, %lld, %lld\n", s, e, leftSize, size, rightSize);*/
    size = size < leftSize ? leftSize : size;
    size = size < rightSize ? rightSize : size;
    return size;
}


int main(){
    int n;
    while(1){
        scanf("%d", &n);
        if(n == 0){
            break;
        }
        for(int i=0; i<n; ++i){
            scanf("%d", &hist[i]);
        }
        long long int s = getMaxSize(0, n-1);
        printf("%lld\n", s);
    }
    return 0;
}

