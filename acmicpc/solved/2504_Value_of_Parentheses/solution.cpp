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
        void clear();
        void print();
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
    delete n;
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

void Stack::print(){
    Node* n = head->n;
    while(n){
        printf("%d\t", n->v);
        n = n->n;
    }
    printf("\n");
}


int stacked(Stack* stack){
    int sum = 0;
    while(stack->top() > 0){
        sum += stack->pop();
    }
    return sum;
}

int main(){
    char s[31];
    int c, v, acc;
    scanf("%s", s);
    int l = strlen(s);
    Stack stack = Stack();
    for(int i=0; i<l; ++i){
        c = - (int) s[i];
        if(c == -40 || c == -91){
            stack.push(c);
        }else if(c == -41){
            acc = stacked(&stack);
            v = stack.pop();
            if(v == -40){
                stack.push(acc ? acc * 2 : 2);
            }else if(v == -91){
                break;
            }
        }else if(c == -93){
            acc = stacked(&stack);
            v = stack.pop();
            if(v == -91){
                stack.push(acc ? acc * 3 : 3);
            }else if(v == -40){
                break;
            }
        }
    }
    int ret = stacked(&stack);
    if(stack.empty()){
        printf("%d\n", ret);
    }else{
        printf("%d\n", 0);
    }
    return 0;
}
