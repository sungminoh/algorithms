/*
 * solution.cpp
 * Copyright (C) 2017 Sungmin <smoh2044@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */

#include <iostream>
#include <vector>
#include <queue>
#include <string>

using namespace std;
typedef vector<vector<int> > Mat;

Mat mat;
queue<pair<int, int> > q;
int n, m;
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

void printMat(){
    for(int i=1; i<=n; ++i){
        for(int j=1; j<=m; ++j){
            printf("%d\t", mat[i][j]);
        }
        printf("\n");
    }
}


void getInput(){
    cin >> n >> m;
    mat.assign(n+5, vector<int>(m+5, 0));
    for(int i=1; i<=n; ++i){
        string s;
        cin >> s;
        for(int j=1; j<=m; ++j){
            mat[i][j] = s[j-1] - '0';
        }
    }
    mat[1][1] = 2;
    q.push({1, 1});
}

void bfs(int i, int j){
    for(int k=0; k<4; ++k){
        int x = i+dx[k];
        int y = j+dy[k];
        if(mat[x][y] == 1){
            mat[x][y] = mat[i][j]+1;
            q.push({x, y});
        }
    }
}

int solve(){
    int i, j;
    while(!q.empty() && !(i==n && j==m)){
        i = q.front().first;
        j = q.front().second;
        bfs(i, j);
        q.pop();
    }
    return mat[n][m]-1;
}

int main(){
    ios_base::sync_with_stdio(false);
    getInput();
    int ans = solve();
    printf("%d\n", ans);

    return 0;
}



