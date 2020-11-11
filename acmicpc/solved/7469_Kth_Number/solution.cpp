/*
 * solution.cpp
 * Copyright (C) 2017 Sungmin <smoh2044@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */

#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;
typedef vector<vector<int> > Mat;


int q(int i, int j, int k){
    return 0;
}

int left(int i){
    return 2*i + 1;
}

int right(int i){
    return 2*i + 2;
}

void printVec(vector<int> v){
    for(auto e : v){
        printf("%d ", e);
    }
    printf("\n");
}

vector<int> mergesort(vector<int> &a, vector<int> &b){
    int n = a.size();
    int m = b.size();
    vector<int> c(n + m);
    int i = 0, j = 0;
    while(i < n && j < m){
        if(a[i] < b[j]){
            c[i+j] = a[i];
            i++;
        }else{
            c[i+j] = b[j];
            j++;
        }
    }
    while(i < n){
        c[i+j] = a[i];
        i++;
    }
    while(j < m){
        c[i+j] = b[j];
        j++;
    }
    return c;
}

vector<int> init(vector<int> &arr, Mat &tree, int n, int s, int e){
    if(s == e){
        return tree[n] = vector<int>(1, arr[s]);
    }else{
        vector<int> l = init(arr, tree, left(n), s, (s+e)/2);
        vector<int> r = init(arr, tree, right(n), (s+e)/2 + 1, e);
        return tree[n] = mergesort(l, r);
    }
}

vector<int> sorted(Mat &tree, int n, int s, int e, int i, int j){
    if(i > e || j < s){
        return vector<int>(0);
    }
    if(i <= s && e <= j){
        return tree[n];
    }
    vector<int> l = sorted(tree, left(n), s, (s+e)/2, i, j);
    vector<int> r = sorted(tree, right(n), (s+e)/2 + 1, e, i, j);
    return mergesort(l, r);
}

void query(Mat &tree, int n, int s, int e, int i, int j, vector<int> &seg){
    if(i > e || j < s){
        return;
    }
    if(i <= s && e <= j){
        seg.push_back(n);
        return;
    }
    query(tree, left(n), s, (s+e)/2, i, j, seg);
    query(tree, right(n), (s+e)/2 + 1, e, i, j, seg);
    return;
}

int binSearch(Mat &tree, vector<int> &seg, int k){
    int l = tree[0].front();
    int r = tree[0].back() + 1;
    int mid;
    while(l < r){
        mid = l + ((r - l) / 2);
        int lower = 0;
        int upper = 0;;
        for(auto i : seg){
            //printf("v: ");
            //printVec(tree[i]);
            lower += (int)(lower_bound(tree[i].begin(), tree[i].end(), mid) - tree[i].begin());
            upper += (int)(upper_bound(tree[i].begin(), tree[i].end(), mid) - tree[i].begin());
        }
        //printf("mid: %d, lower: %d, upper: %d\n", mid, lower, upper);
        if(lower <= k-1 && k <= upper){
            break;
        }else if(lower <= k-1){
            l = mid + 1;
        }else{
            r = mid;
        }
    }
    return mid;
}

int main(){
    int n, m;
    scanf("%d %d", &n, &m);

    vector<int> arr(n);
    for(int i=0; i<n; ++i){
        scanf("%d", &arr[i]);
    }

    int h = (int)ceil(log2(n));
    int treeSize = (1 << (h+1));
    Mat tree(treeSize);

    init(arr, tree, 0, 0, n-1);

    while(m--){
        int i, j, k;
        scanf("%d %d %d", &i, &j, &k);
        vector<int> seg;
        query(tree, 0, 0, n-1, i-1, j-1, seg);
        printf("%d\n", binSearch(tree, seg, k));
        //printf("%d\n", sorted(tree, 0, 0, n-1, i-1, j-1)[k-1]);
    }
    return 0;
}
