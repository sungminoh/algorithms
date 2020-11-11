/*
 * solution.cpp
 * Copyright (C) 2017 Sungmin <smoh2044@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */

#include <iostream>
#include <vector>
#include <queue>
#include <unordered_set>

using namespace std;
typedef vector<vector<vector<int> > > Cube;

int n, m, h;
Cube cube;
queue<vector<int> > q;
int visited = 0;
int vacancy = 0;

void getInput(){
    scanf("%d", &m);
    scanf("%d", &n);
    scanf("%d", &h);
    cube.assign(n+1, vector<vector<int> >(m+1, vector<int>(h+1)));
    for(int k=1; k<=h; ++k){
        for(int i=1; i<=n; ++i){
            for(int j=1; j<=m; ++j){
                scanf("%d", &cube[i][j][k]);
                if(cube[i][j][k] == 1){
                    q.push({i, j, k, 0});
                    visited ++;
                }else if(cube[i][j][k] == -1){
                    vacancy ++;
                }
            }
        }
    }
}

void printcube(){
    for(int k=1; k<=h; ++k){
        for(int i=1; i<=n; ++i){
            for(int j=1; j<=m; ++j){
                printf("%d ", cube[i][j][k]);
            }
            printf("\n");
        }
    }
}

bool pushNeighbor(int i, int j, int k, int d){
    bool inserted = false;
    if(i > 1 && cube[i-1][j][k] == 0){
        visited ++;
        inserted = true;
        q.push({i-1, j, k, d+1});
        cube[i-1][j][k] = 1;
    }
    if(j > 1 && cube[i][j-1][k] == 0){
        visited ++;
        inserted = true;
        q.push({i, j-1, k, d+1});
        cube[i][j-1][k] = 1;
    }
    if(i < n && cube[i+1][j][k] == 0){
        visited ++;
        inserted = true;
        q.push({i+1, j, k, d+1});
        cube[i+1][j][k] = 1;
    }
    if(j < m && cube[i][j+1][k] == 0){
        visited ++;
        inserted = true;
        q.push({i, j+1, k, d+1});
        cube[i][j+1][k] = 1;
    }
    if(k > 1 && cube[i][j][k-1] == 0){
        visited ++;
        inserted = true;
        q.push({i, j, k-1, d+1});
        cube[i][j][k-1] = 1;
    }
    if(k < h && cube[i][j][k+1] == 0){
        visited ++;
        inserted = true;
        q.push({i, j, k+1, d+1});
        cube[i][j][k+1] = 1;
    }
    return inserted;
}

int solve(){
    int ret = 0;
    int n_tocubeos = n*m*h - vacancy;
    while(q.size() && visited < n_tocubeos){
        //printcube();
        //printf("%d\n", ret);
        vector<int> p = q.front(); q.pop();
        //printf("%d %d %d\n", p[0], p[1], p[2]);
        if(pushNeighbor(p[0], p[1], p[2], p[3]) && p[3]+1 > ret){
            ret = p[3]+1;
        }
    }
    if(visited == n_tocubeos) return ret;
    else return -1;
}


int main(){
    getInput();
    int ans = solve();
    printf("%d\n", ans);
    return 0;
}
