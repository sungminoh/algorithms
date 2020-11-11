/*
 * solution.cpp
 * Copyright (C) 2018 sungmin <smoh2044@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */


#include <bits/stdc++.h>


using namespace std;


class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        int n;
        //cout << "checking rows" << endl;
        bool nums[10] = {false};
        for(int i=0; i<9; ++i){
            for(int i=1; i<10; ++i) nums[i] = false;
            for(int j=0; j<9; ++j){
                n = board[i][j] - 48;
                if(n >= 1 && n <= 9){
                    if(nums[n]) return false;
                    else nums[n] = true;
                }
            }
        }
        //cout << "checking columns" << endl;
        for(int i=0; i<9; ++i){
            for(int i=1; i<10; ++i) nums[i] = false;
            for(int j=0; j<9; ++j){
                n = board[j][i] - 48;
                if(n >= 1 && n <= 9){
                    if(nums[n])  return false;
                    else nums[n] = true;
                }
            }
        }
        //cout << "checking boxes" << endl;
        for(int i=0; i<9; i+=3){
            for(int j=0; j<9; j+=3){
                for(int i=1; i<10; ++i) nums[i] = false;
                for(int k=0; k<9; ++k){
                    n = board[j+k/3][i+k%3] - 48;
                    if(n >= 1 && n <= 9){
                        if(nums[n]) return false;
                        else nums[n] = true;
                    }
                }
            }
        }
        return true;
    }
};


vector<vector<char>> getInput(){
    vector<vector<char>> ret(9, vector<char>(9, '.'));
    string s;
    for(int i=0; i<9; ++i){
        cin >> s;
        for(int j=0; j<9; ++j)
            if(s[j] >= 49 && s[j] <= 57)
            ret[i][j] = s[j];
    }
    return ret;
}


void printBoard(vector<vector<char>>& board){
    for_each(board.begin(), board.end(), [](vector<char> row){
            for_each(row.begin(), row.end(), [](char c){
                    cout << c;
                    });
            cout << endl;
            });
}


int main(){
    vector<vector<char>> board = getInput();
    cout << Solution().isValidSudoku(board) << endl;

    return 0;
}
