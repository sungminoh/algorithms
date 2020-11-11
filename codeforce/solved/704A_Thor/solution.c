#include <stdio.h>
#include <string.h>

#define MAX 300000

void printArr(int arr[], int size){
    for(int i=0; i<size; i++){
        printf("%d\t", arr[i]);
    }
}


int main(int argc, char** args){
    int n, q;
    scanf("%d %d", &n, &q);

    int total = 0;

    int notiIdx = 1;
    int idx = 1;
    int noti[MAX+1] = {0};
    int readIdx[MAX+1] = {0};
    int notiCnt[MAX+1] = {0};
    int maxIdx[MAX+1] = {0};

    int sols[q];

    for(int i=0; i<q; i++){
        int type, param;
        scanf("%d %d", &type, &param);
        switch(type){
            case 1:
                total++;
                noti[notiIdx] = param;
                maxIdx[param] = notiIdx;
                notiCnt[param]++;
                notiIdx++;
                break;
            case 2:
                readIdx[param] = maxIdx[param];
                total -= notiCnt[param];
                notiCnt[param] = 0;
                break;
            case 3:
                for(; idx<=param; idx++){
                    int app = noti[idx];
                    if(readIdx[app] >= idx) continue;
                    readIdx[app] = idx;
                    notiCnt[app]--;
                    total--;
                }
                break;
        }
        sols[i] = total;
    }

    for(int i=0; i<q; i++){
        printf("%d\n", sols[i]);
    }

    return 0;
}

