/*
 * solution.cpp
 * Copyright (C) 2017 Sungmin <smoh2044@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */

#include <iostream>
#include <vector>
#include <unordered_set>
#include <tuple>

using namespace std;

typedef vector<pair<int, int> > Graph;

void printVec(vector<int> v){
    for(auto e: v){
        printf("%d ", e);
    }
    printf("\n");
}

void printPairVec(vector<pair<int, int> > v){
    for(auto e: v){
        printf("(%d,%d) ", e.first, e.second);
    }
    printf("\n");
}

pair<Graph, int> getGraph(){
    int n;
    scanf("%d", &n);
    Graph g(n+1);
    unordered_set<int> rootCandidates;
    for(int i=1; i<=n; ++i) rootCandidates.insert(i);
    int e, l, r;
    for(int i=0; i<n; ++i){
        scanf("%d %d %d", &e, &l, &r);
        g[e] = {l, r};
        rootCandidates.erase(l);
        rootCandidates.erase(r);
    }
    return {g, *rootCandidates.begin()};
}

int getPosition(Graph& g, int e, int offset, vector<int>& positions){
    if(e == -1) return 0;
    int l = g[e].first;
    int r = g[e].second;
    int leftWidth = getPosition(g, l, offset, positions);
    int rightWidth = getPosition(g, r, offset+leftWidth+1, positions);
    //printf("getPosition for %d, offset %d\n", e, offset);
    //printf("leftWidth: %d\trightWidth: %d\n", leftWidth, rightWidth);
    positions[e] = offset + leftWidth;
    return leftWidth + rightWidth + 1;
}


void buildBoundary(Graph& g, vector<int>& positions, vector<pair<int, int> >& boundary, int d, int e){
    if(e == -1) return;
    int l = g[e].first;
    int pl = l > 0 ? positions[l] : 0;
    int r = g[e].second;
    int pr = r > 0 ? positions[r] : 0;
    if(boundary[d].first == 0){
        boundary[d]= {pl, pr};
    }else{
        if(pl < boundary[d].first) boundary[d].first = pl;
        if(pr > boundary[d].second) boundary[d].second = pr;
    }
    buildBoundary(g, positions, boundary, d+1, l);
    buildBoundary(g, positions, boundary, d+1, r);
}

pair<int, int> getMaxWidth(vector<pair<int, int> >& boundary){
    int size = boundary.size();
    int m=-1;
    int d=1;
    for(int i=1; boundary[i].second-boundary[i].first+1>0 && i<size; ++i){
        int w = boundary[i].second - boundary[i].first + 1;
        if(boundary[i].first == 0 || boundary[i].second == 0) w = 1;
        if(w > m){
            m = w;
            d = i;
        }
    }
    return {d, m};
}


pair<int, int> solve(Graph& g, int root){
    //printf("root: %d\n", root);
    int n = g.size()-1;
    vector<int> positions(n+1, 0);
    getPosition(g, root, 1, positions);
    //printVec(positions);
    vector<pair<int, int> > boundary(n+1, {n, 0});
    boundary[1] = {0, 1};
    buildBoundary(g, positions, boundary, 2, root);
    //printPairVec(boundary);
    return getMaxWidth(boundary);
}

int numOfNodes(Graph& g, vector<pair<int, int> >& boundary, int offset, int e, int d){
    //printf("numOfNodes(root: %d)\n", e);
    if(e < 0) return 0;
    int leftSize = numOfNodes(g, boundary, offset, g[e].first, d+1);
    //printf("leftSize of %d: %d\n", e, leftSize);
    int p = offset + leftSize+1;
    if(p < boundary[d].first) boundary[d].first = p;
    if(p > boundary[d].second) boundary[d].second = p;
    int rightSize = numOfNodes(g, boundary, offset+leftSize+1, g[e].second, d+1);
    return leftSize + rightSize + 1;
}



pair<int, int> solve2(Graph& g, int root){
    int n = g.size()-1;
    vector<pair<int, int> > boundary(n+1, {n, 0});
    numOfNodes(g, boundary, 0, root, 1);
    //printPairVec(boundary);
    return getMaxWidth(boundary);
}

int main(){
    Graph g;
    int root;
    tie(g, root) = getGraph();
    //printf("root: %d", root);
    //pair<int, int> aws = solve(g, root);
    //printf("%d %d\n", aws.first, aws.second);
    pair<int, int> aws2 = solve2(g, root);
    printf("%d %d\n", aws2.first, aws2.second);
    return 0;
}
