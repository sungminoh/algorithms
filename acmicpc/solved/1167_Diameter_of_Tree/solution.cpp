/*
 * solution.cpp
 * Copyright (C) 2017 Sungmin <smoh2044@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */

#include <iostream>
#include <vector>

using namespace std;
typedef vector<vector<pair<int, int> > > G;


void printG(G& g){
    int n = g.size();
    for(int i=1; i<n; ++i){
        printf("%d: ", i);
        for(auto p : g[i]){
            printf("(%d, %d) ", p.first, p.second);
        }
        printf("\n");
    }
}

G getInput(){
    int n;
    scanf("%d", &n);
    G g(n+1, vector<pair<int, int> >());
    for(int i=0; i<n; ++i){
        int r;
        scanf("%d", &r);
        int v, w;
        scanf("%d", &v);
        while(v > 0){
            scanf("%d", &w);
            g[r].push_back({v, w});
            scanf("%d", &v);
        }
    }
    return g;
}

int dfs(G& g, int r, vector<bool>& visited, int d, int& n, int& m){
    if(d > m){
        m = d;
        n = r;
    }
    int deep = 0;
    for(auto e : g[r]){
        if(visited[e.first]) continue;
        visited[e.first] = true;
        int depth = dfs(g, e.first, visited, d+e.second, n, m);
        if(depth > deep) deep = depth;
    }
    return deep;
}

int solve(G& g){
    int size = g.size();

    vector<bool> visited(size, false);
    int n = 1;
    visited[n] = true;
    int m = -1;
    dfs(g, n, visited, 0, n, m);

    fill(visited.begin(), visited.end(), false);
    visited[n] = true;
    m = -1;
    dfs(g, n, visited, 0, n, m);
    return m;
}

int main(){
    G g = getInput();
    //printG(g);
    int ans = solve(g);
    printf("%d\n", ans);

    return 0;
}
