#include <bits/stdc++.h>

using namespace std;

int n;
double w, v, u, x, y;
double direct, fromPoint, longest, shortest;

double solve(){
    direct = w * v;
    longest = 0;
    shortest = DBL_MAX;
    for(int i=1; i<=n; ++i){
        cin >> x >> y;
        fromPoint = (x * u) + ((w - y) * v);
        if(fromPoint < shortest) shortest = fromPoint;
        else if(fromPoint > longest) longest = fromPoint;
    }
    if(direct <= shortest) return direct;
    else return max(longest, direct);
}

int main(){
    cin >> n >> w >> v >> u;
    cout << fixed << setprecision(6) << solve()/(u*v);
}
