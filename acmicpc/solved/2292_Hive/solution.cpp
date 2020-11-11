#include <bits/stdc++.h>

using namespace std;

int n;
const int MAX = 18258;
int depthUntil[18259];

int biSearch(int n, int* arr){
    int lo = 0, hi = 18259;
    while(lo + 1 < hi){
        int mid = (lo+hi)/2;
        if(arr[mid] < n)
            lo = mid;
        else
            hi = mid;
    }
    return hi;
}

int main(){
    for(int i=1; i<=MAX; ++i){
        depthUntil[i] = 3*i*i - 3*i + 1;
    }

    scanf("%d", &n);

    printf("%d", biSearch(n, depthUntil));

    return 0;
}

