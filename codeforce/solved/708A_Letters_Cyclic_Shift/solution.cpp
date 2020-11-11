#include <bits/stdc++.h>

using namespace std;

void solve(string s){
    bool isStarted = false;
    for(int i=0; i<s.length(); ++i){
        if(!isStarted && s[i] != 'a'){
            isStarted = true;
        }
        if(isStarted){
            if(s[i] == 'a'){
                break;
            }else{
                s[i]--;
            }
        }
    }
    if(!isStarted){
        s[s.length()-1] = 'z';
    }
    cout << s;
}

int main(){
    string s;
    cin >> s;
    solve(s);
}
