/*
 * solution.cpp
 * Copyright (C) 2017 Sungmin <smoh2044@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */

#include <iostream>
#include <vector>
#include <tuple>

using namespace std;

typedef long long LL;

vector<int> getInput(int n){
    vector<int> ret(n);
    for(int i=0; i<n; ++i){
        scanf("%d", &ret[i]);
    }
    return ret;
}


LL getMaxSize(vector<int> &hist, int s, int e){
    if(s == e){
        return hist[s];
    }
    int mid = (e + s)/2;

    LL leftSize = getMaxSize(hist, s, mid);
    LL rightSize = getMaxSize(hist, mid+1, e);

    int minHeight = min(hist[mid], hist[mid+1]);
    LL inter = 2 * minHeight;
    int i=mid-1, j=mid+2;
    while(s <= i || j <= e){
        int leftMinHeight = -1;
        int rightMinHeight = -1;
        LL new_inter = -1;

        if(i >= s){
            leftMinHeight = min(minHeight, hist[i]);
        }else{
            minHeight = min(minHeight, hist[j]);
            new_inter = (LL) minHeight * (j - i);
            inter = max(inter, new_inter);
            j++;
            continue;
        }

        if(j <= e){
            rightMinHeight = min(minHeight, hist[j]);
        }else{
            minHeight = leftMinHeight;
            new_inter = (LL) minHeight * (j - i);
            inter = max(inter, new_inter);
            i--;
            continue;
        }

        if(leftMinHeight > rightMinHeight){
            //printf("to left\n");
            minHeight = leftMinHeight;
            new_inter = (LL) minHeight * (j - i);
            inter = max(inter, new_inter);
            i--;
        }else{
            //printf("to right\n");
            minHeight = rightMinHeight;
            new_inter = (LL) minHeight * (j-i);
            inter = max(inter, new_inter);
            j++;
        }
    }

    LL size = max(max(inter, leftSize), rightSize);
    //printf("[%d, %d] : %lld %lld %lld\n", s, e, leftSize, inter, rightSize);
    return size;
}


int main(){
    int n;
    while(scanf("%d", &n)){
        if(n == 0){
            break;
        }
        vector<int> hist = getInput(n);
        LL s = getMaxSize(hist, 0, hist.size()-1);
        printf("%lld\n", s);
    }
    return 0;
}
