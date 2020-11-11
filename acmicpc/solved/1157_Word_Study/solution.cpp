#include <bits/stdc++.h>

using namespace std;

int cnt[26];
string s;

int main(){
    memset(cnt, 0, 26*sizeof(int));
    getline(cin, s);
    for(int i=0; i<s.length(); ++i){
        if(s[i]>'Z'){
            cnt[s[i]-'a'] ++;
        }else{
            cnt[s[i]-'A'] ++;
        }
    }
    char c = '?';
    int m = 0;
    for(int i=0; i<26; i++){
        if(cnt[i] > m){
            m = cnt[i];
            c = i+'A';
        }else if(cnt[i] == m){
            c = '?';
        }
    }
    printf("%c\n", c);
    return 0;
}

