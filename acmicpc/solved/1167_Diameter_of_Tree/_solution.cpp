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

int setMaxDiameter(G& g, int r, int& m, vector<bool>& visited){
    //printf("root: %d\n", r);
    int l[2] = {0, 0};
    int i=0;
    for(auto e : g[r]){
        int v = e.first;
        int w = e.second;
        if(visited[v]) continue;
        //printf("v: %d\n", v);
        visited[v] = true;
        l[i++] = w + setMaxDiameter(g, v, m, visited);
    }
    int diameter = l[0] + l[1];
    if(diameter > m) m = diameter;
    //printf("%d: %d %d\n", r, l[0], l[1]);
    return max(l[0], l[1]);
}

int findRoot(G& g){
    int size = g.size();
    int i=0;
    for(i=1; i<size; ++i){
        if(g[i].size() < 3) break;
    }
    return i;
}

int solve(G &g){
    int size = g.size();
    int m = -1;
    vector<bool> visited(size, false);
    int r = findRoot(g);
    visited[r] = true;
    setMaxDiameter(g, r, m, visited);
    return m;
}

int main(){
    G g = getInput();
    //printG(g);
    int ans = solve(g);
    printf("%d\n", ans);

    return 0;
}
