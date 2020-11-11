/*
 * solution.cpp
 * Copyright (C) 2017 Sungmin <smoh2044@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */

#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;
typedef vector<vector<int> > Mat;

int n;
Mat mat;
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

void printMat(){
    for(int i=1; i<=n; ++i){
        for(int j=1; j<=n; ++j){
            printf("%d\t", mat[i][j]);
        }
        printf("\n");
    }
}

void getInput(){
    cin >> n;
    mat.assign(n+2, vector<int>(n+2, 0));
    for(int i=1; i<=n; ++i){
        string s;
        cin >> s;
        for(int j=1; j<=n; ++j){
            mat[i][j] = s[j-1] - '0';
        }
    }
}

void dfs(int i, int j, int& s){
    if(mat[i][j] != 1){
        return;
    }
    s++;
    mat[i][j] = s+2;
    for(int k=0; k<4; ++k){
        int x = i+dx[k];
        int y = j+dy[k];
        dfs(x, y, s);
    }
}

void solve(){
    vector<int> chunk;
    for(int i=1; i<=n; ++i){
        for(int j=1; j<=n; ++j){
            if(mat[i][j] != 1) continue;
            int s = 0;
            dfs(i, j, s);
            chunk.push_back(s);
        }
    }
    //printMat();
    sort(chunk.begin(), chunk.end());
    int s = chunk.size();
    cout << s << endl;
    for(int i=0; i<s; ++i){
        cout << chunk[i] << endl;
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    getInput();
    solve();

    return 0;
}
