#include <bits/stdc++.h>

using namespace std;

int n;
int a[100001];

void solve(){
    int startFrom = 1;
    for(int i=1; i<=n; ++i){
        if((a[i] + startFrom) % 2 == 0){
            cout << 2 << endl;
            startFrom = 1;
        }else{
            cout << 1 << endl;
            startFrom = 2;
        }
    }
}

int main(){
    cin >> n;
    for(int i=1; i<=n; ++i) cin >> a[i];
    solve();
}
