#include <bits/stdc++.h>
#define loop(x,n) for(int x = 0; x < n; ++x)
#define MAX LLONG_MAX/2

using namespace std;
typedef long long LL;

int n, c[100001];
string s, r, prevS = "", prevR = "";
LL costS = 0, costR = 0, tmpS, tmpR, cost;

int main(){
    cin >> n;
    loop(i, n) cin >> c[i];
    loop(i, n){
        cin >> s;
        r = s;
        reverse(r.begin(), r.end());
        tmpS = MAX;
        if(prevS.compare(s) <= 0) tmpS = costS;
        if(prevR.compare(s) <= 0) tmpS = min(tmpS, costR);
        tmpR = MAX;
        if(prevS.compare(r) <= 0) tmpR = costS + c[i];
        if(prevR.compare(r) <= 0) tmpR = min(tmpR, costR + c[i]);
        costS = tmpS;
        costR = tmpR;
        prevS = s;
        prevR = r;
    }
    cost = min(costS, costR);
    cout << (cost >= MAX ? -1 : cost);
}
