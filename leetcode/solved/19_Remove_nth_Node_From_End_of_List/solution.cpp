/*
 * solution.cpp
 * Copyright (C) 2018 sungmin <smoh2044@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */

#include <iostream>
#include <vector>
#include <string>
#include <sstream>


using namespace std;


struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};


class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int size = 0;
        ListNode* p = head;
        while(p){
            size++;
            p = p->next;
        }
        int position = size - n;
        ListNode* parent = NULL;
        p = head;
        while(position--){
            parent = p;
            p = p->next;
        }
        if(parent){
            parent->next = p->next;
            delete(p);
        }else{
            head = head->next;
        }
        return head;
    }
};


ListNode* getInput(){
    string s;
    getline(cin, s);
    stringstream ss(s);
    int n;
    ss >> n;
    ListNode* head = new ListNode(n);
    ListNode* p = head;
    while(ss >> n){
        ListNode* node = new ListNode(n);
        p->next = node;
        p = p->next;
    }
    return head;
}

void printList(ListNode* head){
    ListNode* p = head;
    while(p){
        cout << p->val << " ";
        p = p->next;
    }
    cout << endl;
}

int main(){
    ListNode* head = getInput();
    int n;
    cin >> n;
    printList(Solution().removeNthFromEnd(head, n));
    return 0;
}
