#include <bits/stdc++.h>

using namespace std;

int n, x[100001], q, m;
int s, p, e;

int getAnswer(int m){
    s = 1;
    e = n;
    p = (s+e)/2;
    while(s < e-1){
        if(m < x[p]){
            e = p; p = (s+e)/2;
        }else{
            s = p; p = (s+e)/2;
        }
    }
    return m < x[s] ? s-1 : m < x[e] ? s : e;
}

int main(){
    cin >> n;
    for(int i=1; i<=n; ++i){
        cin >> x[i];
    }
    sort(&x[1], &x[1] + n);
    vector<int> answers;
    for(cin >> q; q--; ){
        cin >> m;
        //answers.push_back(getAnswer(m));
        cout << getAnswer(m) << endl;
    }
    //for(auto const& value: answers){
        //cout << value << endl;
    //}
}
