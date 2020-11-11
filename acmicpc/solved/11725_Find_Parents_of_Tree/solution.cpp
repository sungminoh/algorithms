/*
 * solution.cpp
 * Copyright (C) 2017 Sungmin <smoh2044@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */

#include <iostream>
#include <vector>

using namespace std;
typedef vector<vector<int> > Graph;


void printG(Graph &g){
    int n = g.size();
    for(int i=1; i<n; ++i){
        printf("%d: ", i);
        for(auto y : g[i]){
            printf("%d ", y);
        }
        printf("\n");
    }
}

Graph getInput(){
    int n;
    scanf("%d", &n);
    Graph g(n+1, vector<int>());
    for(int i=0; i<n-1; ++i){
        int u, v;
        scanf("%d %d", &u, &v);
        g[u].push_back(v);
        g[v].push_back(u);
    }
    return g;
}


void setParents(Graph& g, vector<int>& parents, int s){
    for(auto e : g[s]){
        if(e == parents[s]) continue;
        parents[e] = s;
        setParents(g, parents, e);
    }
}


vector<int> findParents(Graph& g){
    int n = g.size();
    vector<int> ret(n);
    setParents(g, ret, 1);
    return ret;
}


int main(){
    Graph g = getInput();
    vector<int> parents = findParents(g);
    int n = g.size()-1;
    for(int i=2; i<=n; ++i){
        printf("%d\n", parents[i]);

    }

    return 0;
}
