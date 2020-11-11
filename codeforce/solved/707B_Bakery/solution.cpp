#include <bits/stdc++.h>
#define loop(i, n) for(int i=1; i<=n; i++)

using namespace std;

int n, m, k, u[100001], v[100001], l[100001];
bool s[100001];

int solve(){
    int ret = INT_MAX;
    loop(i, m){
        if(s[u[i]] ^ s[v[i]]) ret = min(ret, l[i]);
    }
    return ret == INT_MAX ? -1 : ret;
}

int main(){
    cin >> n >> m >> k;
    loop(i, m){
        cin >> u[i] >> v[i] >> l[i];
    }
    loop(i, k){
        int city;
        cin >> city;
        s[city] = 1;
    }
    cout << solve();
}
