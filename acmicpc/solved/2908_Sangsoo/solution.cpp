#include <bits/stdc++.h>

using namespace std;

int A, B, a, b;

void printReversed(int n){
    for(; n>0; n/=10){
        printf("%d", n%10);
    }
}

int main(){
    scanf("%d%d", &A, &B);
    for(a=A, b=B; a+b>0; a/=10, b/=10){
        if(a%10 > b%10){
            printReversed(A);
            break;
        }else if(a%10 < b%10){
            printReversed(B);
            break;
        }
    }
    return 0;
}

