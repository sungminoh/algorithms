#include <iostream>
#include <algorithm>
#include <queue>
#include <map>

using namespace std;

void increase(map<int, int>* counter, int v){
    if(counter->find(v) != counter->end()){
        (*counter)[v] ++;
    }else{
        counter->insert(make_pair(v, 1));
    }
}

void decrease(map<int, int>* counter, int v){
    (*counter)[v] --;
    if((*counter)[v] == 0){
        counter->erase(v);
    }
}

int main(){
    int T;
    scanf("%d", &T);
    while(T--){
        int N, M, priority;
        queue<pair<int, int> > l;
        map<int, int> counter;
        scanf("%d %d", &N, &M);
        for(int i=0; i<N; i++){
            scanf("%d", &priority);
            pair<int, int> doc;
            if(i == M){
                doc = make_pair(priority, 1);
            }else{
                doc = make_pair(priority, 0);
            }
            increase(&counter, priority);
            l.push(doc);
        }
        for(int i=1; i<=N; ){
            pair<int, int> doc = l.front(); l.pop();
            if(doc.first < (*counter.rbegin()).first){
                //printf("%d is highest priority\n", (*counter.rbegin()).first);
                //printf("%d is not wiht highest priority move back\n", doc.first);
                l.push(doc);
            }else{
                if(doc.second){
                    //printf("found\n");
                    printf("%d\n", i);
                    break;
                }else{
                    //printf("%d is printed\n", doc.first);
                    decrease(&counter, doc.first);
                    i++;
                }
            }
        }
    }

    return 0;
}


