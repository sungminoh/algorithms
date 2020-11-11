#include <bits/stdc++.h>

int T, h, w, n;

int main(){

    scanf("%d", &T);

    while(T--){
        scanf("%d%d%d", &h, &w, &n);
        n--;
        printf("%d\n", (n%h + 1) * 100 + (n/h + 1));
    }

    return 0;
}
