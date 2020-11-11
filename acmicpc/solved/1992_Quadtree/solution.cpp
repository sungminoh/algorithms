/*
 * solution.cpp
 * Copyright (C) 2017 Sungmin <smoh2044@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */

#include <iostream>
#include <vector>
#include <string>
#include <tuple>

using namespace std;


typedef vector<string> Mat;


void printMat(Mat &m){
    int n = m.size();
    for(int i=0; i<n; ++i){
        for(auto j : m[i]){
            cout << j << ' ';
        }
        cout << endl;
    }
}

Mat getInput(){
    int n, v;
    scanf("%d ", &n);
    Mat mat(n);
    for(int i=0; i<n; ++i){
        cin >> mat[i];
    }
    return mat;
}

pair<string, int> compress(Mat &img, int i1, int j1, int i2, int j2){
    if(i1 == i2 && j1 == j2){
        if(img[i1][j1] == '1'){
            return make_pair("1", 1);
        }else{
            return make_pair("0", -1);
        }
    }
    string slu, slb, sru, srb;
    int ilu, ilb, iru, irb;
    int mid_i = (i1+i2)/2, mid_j = (j1+j2)/2;
    //printf("current; %d %d %d %d\n", i1, j1, i2, j2);
    //printf("l_u; %d %d %d %d\n", i1, j1, mid_i, mid_j);
    tie(slu, ilu) = compress(img, i1, j1, mid_i, mid_j);
    //printf("l_b; %d %d %d %d\n", mid_i, j1, i2, mid_j);
    tie(slb, ilb) = compress(img, mid_i+1, j1, i2, mid_j);
    //printf("r_u;; %d %d %d %d\n", i1, mid_j, mid_i, j2);
    tie(sru, iru) = compress(img, i1, mid_j+1, mid_i, j2);
    //printf("r_b;; %d %d %d %d\n", mid_i, mid_j, i2, j2);
    tie(srb, irb) = compress(img, mid_i+1, mid_j+1, i2, j2);
    //printf("%d %d %d %d\n", ilu, iru, ilb, irb);
    if(ilu == 1 && ilb == 1 && iru == 1 && irb == 1){
        return make_pair("1", 1);
    }else if(ilu == -1 && ilb == -1 && iru == -1 && irb == -1){
        return make_pair("0", -1);
    }else{
        return make_pair("(" + slu + sru + slb + srb + ")", 0);
    }
}


int main(){
    Mat img = getInput();
    //printMat(img);
    int n = img.size();
    string compressed;
    int tmp;
    tie(compressed, tmp) = compress(img, 0, 0, n-1, n-1);
    cout << compressed << endl;

    return 0;
}
