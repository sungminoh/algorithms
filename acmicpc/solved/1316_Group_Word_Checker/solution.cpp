#include <bits/stdc++.h>

using namespace std;

int n, cnt, c;
char previous;
bool appeared[26];
string s;
bool flag = false;

int main(){
    scanf("%d", &n);
    cin.get();
    cnt = 0;
    while(n--){
        previous = -1;
        flag = false;
        memset(appeared, false, 26*sizeof(bool));
        getline(cin, s);
        for(int i=0; i<s.length(); ++i, previous=c){
            c = s[i]-'a';
            if(previous != c){
                if(appeared[c] > 0){
                    break;
                }else if(appeared[c] == 0){
                    appeared[c] = 1;
                }
            }
            if(i == s.length()-1){
                flag = true;
            }
        }
        if(flag){
            cnt++;
        }
    }
    printf("%d", cnt);

    return 0;
}
