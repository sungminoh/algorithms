#include <bits/stdc++.h>

using namespace std;

char s[20], size, sum;
int delay[26] = {3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,8,9,9,9,10,10,10,10};

int main(){
    fgets(s, sizeof(s)/sizeof(*s), stdin);
    size = (int) strlen(s);
    sum = 0;
    for(int i=0; i<size-1; ++i){
        sum += delay[s[i] - 'A'];
    }
    printf("%d", sum);
    return 0;
}

