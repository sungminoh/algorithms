#include <bits/stdc++.h>

using namespace std;

int n;

string getStr(int i){
    if(i % 2 == 0){
        return "I love";
    }else{
        return "I hate";
    }
}

string solve(){
    vector<string> s;
    for(int i=1; i<n; ++i){
        s.push_back(getStr(i));
    }
    stringstream ret;
    copy(s.begin(), s.end(), ostream_iterator<string>(ret, " that "));
    ret << getStr(n) + " it";
    return ret.str();
}

int main(){
    cin >> n;
    cout << solve();
}
