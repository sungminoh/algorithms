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
    ListNode* swapPairs(ListNode* head) {
        if(head == NULL) return head;
        ListNode* p = NULL;
        ListNode* l = head;
        ListNode* r = head->next;
        if(r == NULL) return head;
        l->next = r->next;
        r->next = l;
        ListNode* newHead = r;
        r = l;
        while(r->next && r->next->next){
            p = r;
            l = r->next;
            r = r->next->next;
            p->next = r;
            l->next = r->next;
            r->next = l;
            r = l;
        }
        return newHead;
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
    printList(Solution().swapPairs(head));
    return 0;
}
