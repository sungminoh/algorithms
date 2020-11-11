#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

ll n, s, e, m, p, dst;
ll x[5001];
ll a[5001];
ll b[5001];
ll c[5001];
ll d[5001];
ll nxt[5001];

ll dist(int i, int j){
    return abs(x[i] - x[j]) + (i>j ? c[i]+b[j] : d[i]+a[j]);
}

ll solve(){
    ll ret = dist(s, e);
    nxt[s] = e;
    for(int i=1; i<=n; ++i){
        if(i == s || i == e) continue;
        m = LLONG_MAX;
        for(int j=s; j!=e; j=nxt[j]){
            dst = dist(j, i) + dist(i, nxt[j]) - dist(j, nxt[j]);
            if(dst < m){
                m = dst;
                p = j;
            }
        }
        ret += m;
        nxt[i] = nxt[p];
        nxt[p] = i;
    }
    return ret;
}

int main(){
    cin  >> n >> s >> e;
    for(int i=1; i<=n; ++i) cin >> x[i];
    for(int i=1; i<=n; ++i) cin >> a[i];
    for(int i=1; i<=n; ++i) cin >> b[i];
    for(int i=1; i<=n; ++i) cin >> c[i];
    for(int i=1; i<=n; ++i) cin >> d[i];

    cout << solve();
}
