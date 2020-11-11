#include <iostream>
#include <cstring>

using namespace std;


struct Node{
    int v;
    Node* b;
    Node* n;
};

class Deque{
    public:
        Deque();
        void push_front(int v);
        void push_back(int v);
        int pop_front();
        int pop_back();
        int size();
        int empty();
        int front();
        int back();
        void printAll();
    private:
        Node* newNode(int v, Node* b, Node* n);
        int _size;
        Node* head;
        Node* tail;
};

Node* Deque::newNode(int v, Node* b, Node* n){
    Node* node = new Node;
    node->v = v;
    node->b = b;
    node->n = n;
    return node;
}

Deque::Deque(){
    head = newNode(-1, NULL, NULL);
    tail = head;
    _size = 0;
}

void Deque::push_front(int v){
    Node* n = newNode(-1, NULL, head);
    head->v = v;
    head->b = n;
    head = n;
    _size++;
}

void Deque::push_back(int v){
    Node* n = newNode(v, tail, NULL);
    tail->n = n;
    tail = n;
    _size++;
}

int Deque::pop_front(){
    if(_size == 0) return -1;
    Node* n = head->n;
    int v = n->v;
    n->b = NULL;
    delete head;
    head = n;
    _size--;
    return v;
}

int Deque::pop_back(){
    if(_size == 0) return -1;
    Node* n = tail;
    tail = n->b;
    tail->n = NULL;
    int v = n->v;
    delete n;
    _size--;
    return v;
}

int Deque::size(){
    return _size;
}

int Deque::empty(){
    return _size == 0 ? 1 : 0;
}

int Deque::front(){
    return _size != 0 ? head->n->v : -1;
}

int Deque::back(){
    return _size != 0 ? tail->v : -1;
}

void Deque::printAll(){
    printf("-------------------------\n");
    Node* n = head->n;
    while(n){
        printf("%d\t", n->v);
        n = n->n;
    }
    printf("\n");
    n = tail;
    while(n != head){
        printf("%d\t", n->v);
        n = n->b;
    }
    printf("\n");
    printf("-------------------------\n");
}


int main(){
    int N, n;
    char command[15];
    scanf("%d", &N);

    Deque deque = Deque();
    while(N--){
        scanf("%s", command);
        if(strcmp(command, "push_front") == 0){
            scanf("%d", &n);
            deque.push_front(n);
        }else if(strcmp(command, "push_back") == 0){
            scanf("%d", &n);
            deque.push_back(n);
        }else if(strcmp(command, "pop_front") == 0){
            printf("%d\n", deque.pop_front());
        }else if(strcmp(command, "pop_back") == 0){
            printf("%d\n", deque.pop_back());
        }else if(strcmp(command, "size") == 0){
            printf("%d\n", deque.size());
        }else if(strcmp(command, "empty") == 0){
            printf("%d\n", deque.empty());
        }else if(strcmp(command, "front") == 0){
            printf("%d\n", deque.front());
        }else if(strcmp(command, "back") == 0){
            printf("%d\n", deque.back());
        }
    }

    return 0;
}
