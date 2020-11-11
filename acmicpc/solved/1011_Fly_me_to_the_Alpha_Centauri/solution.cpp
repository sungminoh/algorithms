#include <bits/stdc++.h>

using namespace std;

int T, x, y, d, n;

int main(){
    scanf("%d", &T);
    while(T--){
        scanf("%d%d", &x, &y);
        d = y-x;

        n = sqrt(d);

        if(pow(n, 2) == d){
            printf("%d\n", 2*n-1);
        }
        else if(pow(n, 2) + n >= d){
            printf("%d\n", 2*n);
        }else{
            printf("%d\n", 2*n+1);
        }

    }
    return 0;
}
