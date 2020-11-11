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
typedef vector<vector<int> > Mat;

int n, m;
Mat mat;
queue<vector<int> > q;
int visited = 0;
int vacancy = 0;

void getInput(){
    scanf("%d", &m);
    scanf("%d", &n);
    mat.assign(n+1, vector<int>(m+1));
    for(int i=1; i<=n; ++i){
        for(int j=1; j<=m; ++j){
            scanf("%d", &mat[i][j]);
            if(mat[i][j] == 1){
                q.push({i, j, 0});
                visited ++;
            }else if(mat[i][j] == -1){
                vacancy ++;
            }
        }
    }
}

void printMat(){
    for(int i=1; i<=n; ++i){
        for(int j=1; j<=m; ++j){
            printf("%d ", mat[i][j]);
        }
        printf("\n");
    }
}

bool pushNeighbor(int i, int j, int d){
    bool inserted = false;
    if(i > 1 && mat[i-1][j] == 0){
        visited ++;
        inserted = true;
        q.push({i-1, j, d+1});
        mat[i-1][j] = 1;
    }
    if(j > 1 && mat[i][j-1] == 0){
        visited ++;
        inserted = true;
        q.push({i, j-1, d+1});
        mat[i][j-1] = 1;
    }
    if(i < n && mat[i+1][j] == 0){
        visited ++;
        inserted = true;
        q.push({i+1, j, d+1});
        mat[i+1][j] = 1;
    }
    if(j < m && mat[i][j+1] == 0){
        visited ++;
        inserted = true;
        q.push({i, j+1, d+1});
        mat[i][j+1] = 1;
    }
    return inserted;
}

int solve(){
    int ret = 0;
    int n_tomatos = n*m - vacancy;
    while(q.size() && visited < n_tomatos){
        //printMat();
        //printf("%d\n", ret);
        vector<int> p = q.front(); q.pop();
        //printf("%d %d %d\n", p[0], p[1], p[2]);
        if(pushNeighbor(p[0], p[1], p[2]) && p[2]+1 > ret){
            ret = p[2]+1;
        }
    }
    if(visited == n_tomatos) return ret;
    else return -1;
}


int main(){
    getInput();
    int ans = solve();
    printf("%d\n", ans);
    return 0;
}
