#include <bits/stdc++.h>
#define loop(i, n) for(int i=1; i<=n; ++i)

using namespace std;
typedef long long LL;

void solve(LL n){
    if(n <= 2){
        printf("-1");
        return;
    }
    if(n % 2 == 1){
        LL m = n*n;
        cout << m/2 << " " << m-(m/2);
    }else{
        LL m = (n/2)*(n/2);
        cout << m-1 << " " << m+1;
    }
}

int main(){
    LL n;
    cin >> n;
    solve(n);
}
