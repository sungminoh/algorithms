#include <iostream>
#include <cstring>
#include <stack>
#include <queue>
#include <set>

using namespace std;

void dfs(set<int> graph[], int v){
    set<int> visited;
    stack<int> waitings;
    waitings.push(v);
    while(!waitings.empty()){
        v = waitings.top(); waitings.pop();
        if(visited.find(v) != visited.end()) continue;
        visited.insert(v);
        printf("%d ", v);
        for(set<int>::reverse_iterator it=graph[v].rbegin(); it!=graph[v].rend(); ++it){
            if(visited.find(*it) != visited.end()) continue;
            waitings.push(*it);
        }
    }
    printf("\n");
}

void bfs(set<int> graph[], int v){
    set<int> visited;
    queue<int> waitings;
    waitings.push(v);
    while(!waitings.empty()){
        v = waitings.front(); waitings.pop();
        if(visited.find(v) != visited.end()) continue;
        visited.insert(v);
        printf("%d ", v);
        for(set<int>::iterator it=graph[v].begin(); it!=graph[v].end(); ++it){
            if(visited.find(*it) != visited.end()) continue;
            waitings.push(*it);
        }
    }
    printf("\n");
}


int main(){
    int N, M, V;
    set<int> graph[1001];
    scanf("%d %d %d", &N, &M, &V);

    for(int i=0; i<M; i++){
        int u, v;
        scanf("%d %d", &u, &v);
        graph[u].insert(v);
        graph[v].insert(u);
    }

    dfs(graph, V);
    bfs(graph, V);

    return 0;
}
