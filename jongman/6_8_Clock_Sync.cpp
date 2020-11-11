#include <iostream>

using namespace std;

const int MAX = 987654321;
const int NUMBER_OF_CLOCKS = 16;
const int NUMBER_OF_SWITCHES = 10;
bool switches[NUMBER_OF_SWITCHES][NUMBER_OF_CLOCKS] = {
    {1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0},
    {0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1},
    {1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0},
    {1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1},
    {0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1},
    {0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1},
    {0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0}
};

void printArr(int arr[16]){
    for(int i=0; i<16; ++i){
        printf("%d ", arr[i]);
    }
    printf("\n");
}


bool areAligned(int clocks[16]){
    for(int i=0; i<NUMBER_OF_CLOCKS; ++i){
        if(clocks[i] != 0){
            return false;
        }
    }
    return true;
}

void push(int clocks[16], int n){
    for(int i=0; i<NUMBER_OF_CLOCKS; ++i){
        if(switches[n][i]){
            clocks[i] += 3;
            clocks[i] %= 12;
        }
    }
}

int getAnswer(int clocks[16], int n){
    if(n == NUMBER_OF_SWITCHES){
        return areAligned(clocks) ? 0 : MAX;
    }
    int ret = MAX;
    for(int i=0; i<4; ++i){
        ret = min(ret, i + getAnswer(clocks, n+1));
        push(clocks, n);
    }
    return ret;
}


int main(){
    int c;
    scanf("%d", &c);
    while(c--){
        int clocks[NUMBER_OF_CLOCKS];
        for(int i=0; i<NUMBER_OF_CLOCKS; ++i){
            scanf("%d", &clocks[i]);
            clocks[i] %= 12;
        }
        int ans = getAnswer(clocks, 0);
        printf("%d\n", ans == MAX? -1 : ans);
    }

    return 0;
}
