#include <iostream>
#include <deque>
#include <stdlib.h>

using namespace std;


void print(deque<int> deq){
    for(deque<int>::iterator it=deq.begin(); it!=deq.end(); ++it){
        printf("%d ", *it);
    }
    printf("\n");
}

int main(){
    int N, M;
    scanf("%d %d", &N, &M);

    int* tmp = (int*) malloc(sizeof(int) * N);
    for(int i=0; i<N; ++i){
        tmp[i] = 0;
    }
    for(int i=1; i<=M; ++i){
        int n;
        scanf("%d", &n);
        tmp[n-1] = i;
    }

    deque<int> deq;
    for(int i=0; i<N; ++i){
        deq.push_back(tmp[i]);
    }

    int cnt=0;
    for(int i=1; i<=M; ++i){
        //printf("deq: "); print(deq);
        //printf("cnt: %d\n", cnt);
        int cntBefore=0;
        for(deque<int>::iterator it=deq.begin(); it!=deq.end(); ++it, ++cntBefore){
            if(*it == i){
                int cntBehind = deq.size() - cntBefore;
                if(cntBefore <= cntBehind){
                    while(deq.front() != i){
                        int tmp = deq.front(); deq.pop_front();
                        deq.push_back(tmp);
                        cnt++;
                    }
                    deq.pop_front();
                }else{
                    while(deq.front() != i){
                        int tmp = deq.back(); deq.pop_back();
                        deq.push_front(tmp);
                        cnt++;
                    }
                    deq.pop_front();
                }
                break;
            }
        }
    }

    printf("%d\n", cnt);

    return 0;
}
