#include <iostream>
#include <string>

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
        void clear();
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

void Stack::clear(){
    while(pop() != -1){
    }
}


int main(){
    int N;
    char ps[55];
    scanf("%d ", &N);

    Stack stack = Stack();
    while(N--){
        stack.clear();
        scanf("%s", ps);
        bool isValid = true;
        for(int i=0; ps[i]!='\0'; ++i){
            char p = ps[i];
            if(p == '('){
                stack.push('(');
            }else{
                if(stack.pop() != '('){
                    isValid = false;
                    break;
                }
            }
        }
        if(isValid && stack.size() == 0){
            printf("YES\n");
        }else{
            printf("NO\n");
        }
    }
    return 0;
}
