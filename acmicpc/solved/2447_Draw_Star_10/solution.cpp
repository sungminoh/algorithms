/*
 * solution.cpp
 * Copyright (C) 2017 Sungmin <smoh2044@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */

#include <iostream>
#include <string>
#include <vector>

using namespace std;

typedef vector<vector<char> > Mat;


void fillIn(Mat &board, int i, int j, int x, int y, int p){
    if(p == 5){
        return;
    }
    if(i == x && j == y){
        board[i][j] = '*';
        return;
    }
    int r1 = (2*i + x)/3;
    int r2 = (i + 2*x)/3;
    int c1 = (2*j + y)/3;
    int c2 = (j + 2*y)/3;
    fillIn(board, i, j, r1, c1, 1);
    fillIn(board, i, c1+1, r1, c2, 2);
    fillIn(board, i, c2+1, r1, y, 3);
    fillIn(board, r1+1, j, r2, c1, 4);
    fillIn(board, r1+1, c1+1, r2, c2, 5);
    fillIn(board, r1+1, c2+1, r2, y, 6);
    fillIn(board, r2+1, j, x, c1, 7);
    fillIn(board, r2+1, c1+1, x, c2, 8);
    fillIn(board, r2+1, c2+1, x, y, 9);
}

void printStar(int n){
    Mat board(n, vector<char>(n, ' '));
    fillIn(board, 0, 0, n-1, n-1, 1);
    for(vector<char> row : board){
        for(char e : row){
            printf("%c", e);
        }
        printf("\n");
    }
}


int main(){
    int n;
    scanf("%d", &n);
    printStar(n);

    return 0;
}
