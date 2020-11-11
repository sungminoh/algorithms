#include <iostream>

using namespace std;

char evaluate(int sticks[4]){
    int cnt = 0;
    for(int i=0; i<4; ++i){
        if(sticks[i]) cnt++;
    }
    switch(cnt){
        case 0:
            return 'D';
        case 1:
            return 'C';
        case 2:
            return 'B';
        case 3:
            return 'A';
        case 4:
            return 'E';
        default:
            return -1;
    }
}

int main(){
    for(int t=0; t<3; ++t){
        int sticks[4];
        for(int i=0; i<4; ++i){
            scanf("%d", &sticks[i]);
        }
        printf("%c\n", evaluate(sticks));
    }
    return 0;
}
