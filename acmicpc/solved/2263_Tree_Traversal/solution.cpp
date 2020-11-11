/*
 * solution.cpp
 * Copyright (C) 2017 Sungmin <smoh2044@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */

#include <iostream>
#include <vector>

using namespace std;


struct Node {
    int v;
    Node* l;
    Node* r;
};

vector<int> getInput(int n){
    vector<int> ret(n);
    for(int i=0; i<n; ++i){
        scanf("%d", &ret[i]);
    }
    return ret;
}


Node* construct(vector<int> &inorder, int is, int ie, vector<int> &postorder, int ps, int pe){
    Node* node = new Node;
    if(is > ie){
        return NULL;
    }
    if(is == ie){
        node->v = inorder[is];
        return node;
    }
    int root = postorder[pe];
    node->v = root;
    int i=0;
    for(; i<=ie-is; ++i){
        if(inorder[is+i] == root){
            break;
        }
    }
    node->l = construct(inorder, is, is+i-1, postorder, ps, ps+i-1);
    node->r = construct(inorder, is+i+1, ie, postorder, ps+i, pe-1);
    return node;
}


void printPreorder(Node* tree){
    if(tree == NULL)
        return;
    printf("%d ", tree->v);
    printPreorder(tree->l);
    printPreorder(tree->r);
}


void printVec(vector<int> &v){
    for(auto e: v){
        cout << e << " ";
    }
    cout << endl;
}

int main(){
    int n;
    scanf("%d", &n);
    vector<int> inorder = getInput(n);
    vector<int> postorder = getInput(n);
    //printVec(inorder);
    //printVec(postorder);
    Node* tree = construct(inorder, 0, n-1, postorder, 0, n-1);
    printPreorder(tree);
    return 0;
}
