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
    int N, number;
    char command[10];
    scanf("%d", &N);

    Stack stack = Stack();
    while(N--){
        scanf("%s", command);
        if(strcmp(command, "push") == 0){
            scanf("%d ", &number);
            stack.push(number);
        }else if(strcmp(command, "pop") == 0){
            printf("%d\n", stack.pop());
        }else if(strcmp(command, "size") == 0){
            printf("%d\n", stack.size());
        }else if(strcmp(command, "empty") == 0){
            printf("%d\n", stack.empty());
        }else if(strcmp(command, "top") == 0){
            printf("%d\n", stack.top());
        }
    }
    return 0;
}
