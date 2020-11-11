#include <iostream>
#include <cstring>

using namespace std;


struct Node{
    int v;
    Node* b;
    Node* n;
};

class Queue{
    public:
        Queue();
        void push(int v);
        int pop();
        int size();
        int empty();
        int front();
        int back();
    private:
        Node* newNode(int v, Node* b, Node* n);
        int _size;
        Node* head;
        Node* tail;
};

Node* Queue::newNode(int v, Node* b, Node* n){
    Node* node = new Node;
    node->v = v;
    node->b = b;
    node->n = n;
    return node;
}

Queue::Queue(){
    head = newNode(-1, NULL, NULL);
    tail = head;
    _size = 0;
}

void Queue::push(int v){
    Node* n = newNode(v, tail, NULL);
    tail->n = n;
    tail = n;
    _size ++;
}

int Queue::pop(){
    if(head == tail) return -1;
    Node* n = head->n;
    int v = n->v;
    n->b = NULL;
    delete head;
    head = n;
    _size --;
    return v;
}

int Queue::size(){
    return _size;
}

int Queue::empty(){
    return _size ? 0 : 1;
}

int Queue::front(){
    return _size != 0 ? head->n->v : -1;
}

int Queue::back(){
    return _size != 0 ? tail->v : -1;
}

int main(){
    int N, number;
    char command[10];
    scanf("%d", &N);

    Queue queue = Queue();
    while(N--){
        scanf("%s", command);
        if(strcmp(command, "push") == 0){
            scanf("%d", &number);
            queue.push(number);
        }else if(strcmp(command, "pop") == 0){
            printf("%d\n", queue.pop());
        }else if(strcmp(command, "size") == 0){
            printf("%d\n", queue.size());
        }else if(strcmp(command, "empty") == 0){
            printf("%d\n", queue.empty());
        }else if(strcmp(command, "front") == 0){
            printf("%d\n", queue.front());
        }else if(strcmp(command, "back") == 0){
            printf("%d\n", queue.back());
        }
    }
    return 0;
}
