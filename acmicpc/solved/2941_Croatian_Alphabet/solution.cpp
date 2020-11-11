#include <bits/stdc++.h>

using namespace std;

char s[105], answer;

int main(){
    scanf("%s", &s);
    int len = strlen(s);
    answer = len;
    for(int i=1; i<len; i++){
        if(s[i]=='=' && i>=2 && (s[i-1]=='z' && s[i-2]=='d')) answer -= 2;
        else if(s[i]=='=' && (s[i-1]=='c' || s[i-1]=='s' || s[i-1]=='z')) answer -= 1;
        else if(s[i]=='-' && (s[i-1]=='c' || s[i-1]=='d')) answer -= 1;
        else if(s[i]=='j' && (s[i-1]=='l' || s[i-1]=='n')) answer -= 1;
    }
    printf("%d", answer);
    return 0;
}

