#include <bits/stdc++.h>

using namespace std;

int n;
double a, b, x, y, v, m = DBL_MAX;

double distToNext(){
    cin >> x >> y >> v;
    return sqrt(pow(x-a, 2) + pow(y-b, 2)) / v;
}

int main(){
    cin >> a >> b;
    for(cin >> n; n--;){
        m = min(m, distToNext());
    }
    cout << fixed << setprecision(7) << m;
}

