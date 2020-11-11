#include <bits/stdc++.h>

using namespace std;

int T, R;
string S;

int main(){
    scanf("%d", &T);
    while(T--){
        scanf("%d", &R);
        getline(cin, S);
        for(int i = 1; i<S.length(); ++i){
            for(int j=0; j<R; ++j){
                printf("%c", S[i]);
            }
        }
        printf("\n");
    }
    return 0;
}
