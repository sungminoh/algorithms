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
    void rotateLayer(vector<vector<int>>& m, int i, int j, int n){
        if(n == 1) return;
        for(int t=0; t<n-1; ++t){
            int tmp = m[j][i+n-1];
            for(int k=i+n-1; k>i; --k){
                m[j][k] = m[j][k-1];
            }
            for(int k=j; k<j+n-1; ++k){
                m[k][i] = m[k+1][i];
            }
            for(int k=i; k<i+n-1; ++k){
                m[j+n-1][k] = m[j+n-1][k+1];
            }
            for(int k=j+n-1; k>j+1; --k){
                m[k][i+n-1] = m[k-1][i+n-1];
            }
            m[j+1][i+n-1] = tmp;
        }
    }

    void rotateLayer2(vector<vector<int>>& m, int i, int j, int n){
        if(n==1) return;
        for(int k=0; k<n-1; ++k){
            int tmp = m[j][i+n-1-k];
            m[j][i+n-1-k] = m[j+k][i];
            m[j+k][i] = m[j+n-1][i+k];
            m[j+n-1][i+k] = m[j+n-1-k][i+n-1];
            m[j+n-1-k][i+n-1] = tmp;
        }
    }

    void rotate(vector<vector<int>>& matrix) {
        int size = matrix.size();
        for(int i=0; i<size/2; ++i){
            //rotateLayer(matrix, i, i, size-2*i);
            rotateLayer2(matrix, i, i, size-2*i);
        }
    }
};


vector<int> getVec(){
    string s;
    getline(cin, s);
    stringstream ss(s);
    vector<int> v;
    int n;
    while(ss >> n)
        v.push_back(n);
    return v;
}

vector<vector<int>> getMat(){
    vector<vector<int>> ret;
    vector<int> v = getVec();
    ret.push_back(v);
    int n = v.size();
    while(--n)
        ret.push_back(getVec());
    return ret;
}


string join(vector<int>& v, string delim){
    stringstream ss;
    for_each(v.begin(), v.end()-1, [&](int x){ss << to_string(x) << delim;});
    ss << *v.rbegin();
    return ss.str();
}

int main(){
    vector<vector<int>> mat = getMat();
    Solution().rotate(mat);
    for(auto v: mat){
        cout << join(v, " ") << endl;
    }

    return 0;
}
