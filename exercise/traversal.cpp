/*
 * solution.cpp
 * Copyright (C) 2017 Sungmin <smoh2044@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */

#include <iostream>
#include <unordered_map>

using namespace std;

typedef pair<char, char> Branch;
typedef unordered_map<char, Branch> Tree;

void preorder(Tree &tree, char s){
    printf("%c", s);
    if(tree[s].first != '.') preorder(tree, tree[s].first);
    if(tree[s].second != '.') preorder(tree, tree[s].second);
}

void inorder(Tree &tree, char s){
    if(tree[s].first != '.') inorder(tree, tree[s].first);
    printf("%c", s);
    if(tree[s].second != '.') inorder(tree, tree[s].second);
}

void postorder(Tree &tree, char s){
    if(tree[s].first != '.') postorder(tree, tree[s].first);
    if(tree[s].second != '.') postorder(tree, tree[s].second);
    printf("%c", s);
}


int main(){
    int n;
    scanf("%d", &n);
    Tree tree;
    for(int i=0; i<n; ++i){
        char p, l, r;
        getchar();
        scanf("%c %c %c", &p, &l, &r);
        tree[p] = {l, r};
    }

    preorder(tree, 'A'); printf("\n");
    inorder(tree, 'A'); printf("\n");
    postorder(tree, 'A'); printf("\n");



    return 0;
}
