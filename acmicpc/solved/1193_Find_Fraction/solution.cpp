#include <bits/stdc++.h>

using namespace std;

int x, s, i;

int main(){
    scanf("%d", &x);
    for(i=0, s=0; s<x; i++){
        s+=i+1;
    }
    if(i%2 == 0){
        printf("%d/%d", i-(s-x), 1+(s-x));
    }else{
        printf("%d/%d", 1+(s-x), i-(s-x));
    }
    return 0;
}
