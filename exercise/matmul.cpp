/*
 * solution.cpp
 * Copyright (C) 2017 Sungmin <smoh2044@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */

#include <iostream>
#include <vector>

using namespace std;


typedef vector<vector<int> > Mat;


void printMat(Mat &mat){
    int n = mat.size(), m = mat[0].size();
    for(int i=0; i<n; ++i){
        for(int j=0; j<m-1; ++j){
            printf("%d ", mat[i][j]);
        }
        printf("%d\n", mat[i][m-1]);
    }
}

Mat getMatrix(){
    int n, m;
    scanf("%d %d", &n, &m);
    Mat mat(n, vector<int>(m));
    for(int i=0; i<n; ++i){
        for(int j=0; j<m; ++j){
            scanf("%d", &mat[i][j]);
        }
    }
    return mat;
}

Mat dot(Mat &a, Mat &b){
    int n = a.size(), m = b.size(), k = b[0].size();
    Mat ret(n, vector<int>(k, 0));
    for(int i=0; i<n; ++i){
        for(int j=0; j<m; ++j){
            for(int h=0; h<k; ++h){
                ret[i][h] += a[i][j]*b[j][h];
            }
        }
    }
    return ret;
}

int main(){
    Mat a = getMatrix();
    Mat b = getMatrix();
    Mat c = dot(a, b);
    printMat(c);

    return 0;
}
