#include <iostream>
#include <cstring>

using namespace std;


struct Node{
    int v;
    Node* b;
    Node* n;
};

class Stack{
    public:
        Stack();
        void push(int v);
        int pop();
        int size();
        int empty();
        int top();
    private:
        int _size;
        Node* head;
        Node* tail;
};

Stack::Stack(){
    head = new Node;
    tail = head;
    _size = 0;
}

void Stack::push(int v){
    Node* n = new Node;
    n->v = v;
    n->b = tail;
    tail->n = n;
    tail = n;
    _size++;
}

int Stack::pop(){
    if(tail == head) return -1;
    Node* n = tail;
    int v = n->v;
    tail = n->b;
    tail->n = NULL;
    delete(n);
    _size--;
    return v;
}

int Stack::size(){
    return _size;
}

int Stack::empty(){
    return _size ? 0 : 1;
}

int Stack::top(){
    if(tail == head) return -1;
    return tail->v;
}


int main(){
    int N, n;
    scanf("%d", &N);
    char commands[200000];

    Stack stack = Stack();
    int k = 1;
    int j = 0;
    bool isSuccess = true;
    while(N--){
        scanf("%d", &n);
        if(stack.top() < n){
            while(stack.top() < n){
                stack.push(k++);
                commands[j++] = '+';
            }
        }
        if(stack.top() == n){
            stack.pop();
            commands[j++] = '-';
        }else{
            isSuccess = false;
        }
    }
    if(isSuccess){
        for(int i=0; i<j; ++i){
            printf("%c\n", commands[i]);
        }
    }else{
        printf("NO");
    }
    return 0;
}
