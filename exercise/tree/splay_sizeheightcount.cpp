#include <iostream>
#include <algorithm>
#include <cstring>
#include <cassert>

typedef long long LL;

using namespace std;

struct Node{
    int value;
    Node* parent;
    Node* left;
    Node* right;
    int cnt;
    int size;
    int height;
};

const bool DEBUG = true;

void print(string s){
    if(DEBUG) printf("%s", s.c_str());
}

void printNode(Node* n){
    if(DEBUG){
        if(n == NULL){
            printf("Node(NULL)\n");
        }else{
            printf("Node(v: %d, c: %d, s: %d, p: %d, l: %d(%d), r: %d(%d), h:%d)\n",
                    n->value, n->cnt, n->size,
                    n->parent ? n->parent->value : -1,
                    n->left ? n->left->value : -1,
                    n->left ? n->left->size : 0,
                    n->right ? n->right->value : -1,
                    n->right ? n->right->size : 0,
                    n->height);
        }
    }
}

class Tree{
    public:
        Tree();
        Node* root;
        void insert(int value);
        Node* search(int value);
        Node* remove(Node* base, int value);
        Node* findMid();
        void splay(Node* n);
    private:
        Node* newNode(int value);
        int getSize(Node* n);
        int getHeight(Node* n);
        void update(Node* base, Node *n);
        bool isLeft(Node* n);
        bool isRight(Node* n);
        Node* replace(Node* n, Node* r);
        Node* findSuccessor(Node* n);
        Node* findPredecessor(Node* n);
        void rotate(Node* n);
};

Tree::Tree(){
    root = NULL;
}

int Tree::getSize(Node* n){
    return n == NULL ? 0 : n->size;
}

int Tree::getHeight(Node* n){
    return n == NULL ? 0 : n->height;
}

//int Tree::getCnt(Node*){
    //return n == NULL ? 0 : n->cnt;
//}

bool Tree::isLeft(Node* n){
    return n->parent != NULL ? n->parent->left == n : false;
}

bool Tree::isRight(Node* n){
    return n->parent != NULL ? n->parent->right == n : false;
}


Node* Tree::newNode(int value){
    Node* n = new Node;
    n->value = value;
    n->parent = NULL;
    n->left = NULL;
    n->right = NULL;
    n->cnt = 1;
    n->size = 1;
    n->height = 1;
    return n;
}

void Tree::insert(int value){
    //print("insert\t... ");
    // when root is NULL
    if(root == NULL){
        Node* n = newNode(value);
        root = n;
    }else{
        // find appropriate position and insert
        Node* base = root;
        while(true){
            base->size ++;
            if(value < base->value){
                if(base->left == NULL){
                    Node* n = newNode(value);
                    base->left = n;
                    n->parent = base;
                    break;
                }
                base = base->left;
            }else if(base->value < value){
                if(base->right == NULL){
                    Node* n = newNode(value);
                    base->right = n;
                    n->parent = base;
                    break;
                }
                base = base->right;
            }else{
                base->cnt ++;
                break;
            }
        }
        update(root, base);
    }
    //print("done\n");
}

void Tree::update(Node* base, Node* n){
    //print("update\t... ");
    while(true){
        //print(". ");
        n->size = getSize(n->left) + n->cnt + getSize(n->right);
        n->height = max(getHeight(n->left), getHeight(n->right)) + 1;
        if(n == base) break;
        n = n->parent;
    }
    //print("done\n");
}

Node* Tree::search(int value){
    //print("search\n");
    Node* n = root;
    while(n != NULL){
        if(value < n->value){
            n = n->left;
        }else if(value > n->value){
            n = n->right;
        }else{
            return n;
        }
    }
    return NULL;
}

Node* Tree::replace(Node* n, Node* r){
    //print("replace\t... ");
    if(r != NULL){
        r->parent = n->parent;
    }
    if(isLeft(n)){
        n->parent->left = r;
    }else if(isRight(n)){
        n->parent->right = r;
    }else{
        root = r;
    }
    //print("done\n");
    return r;
}

Node* Tree::findSuccessor(Node* n){
    //print("findSuccessor\n");
    assert(n != NULL);
    Node* rightBranch = n->right;
    if(rightBranch == NULL){
        return NULL;
    }
    while(rightBranch->left!= NULL){
        rightBranch = rightBranch->left;
    }
    return rightBranch;
}

Node* Tree::findPredecessor(Node* n){
    //print("findPredecessor\n");
    assert(n != NULL);
    Node* leftBranch = n->left;
    if(leftBranch == NULL){
        return NULL;
    }
    while(leftBranch->right != NULL){
        leftBranch = leftBranch->right;
    }
    return leftBranch;
}

Node* Tree::remove(Node* base, int value){
    //if(DEBUG) printf("remove %d from ", value);
    //printNode(base);
    if(base == NULL){
        //print("\tcouldn't find\n");
        return base;
    }
    if(value < base->value){
        //if(DEBUG) printf("\t%d is smaller than base\n", value);
        base->left = remove(base->left, value);
    }else if(base->value < value){
        //if(DEBUG) printf("\t%d is bigger than base\n", value);
        base->right = remove(base->right, value);
    }else{
        if(base->cnt > 1){
            //printf("\tdeduct count\n");
            base->cnt --;
        }else{
            if(base->left == NULL){
                Node* rightBranch = replace(base, base->right);
                delete(base);
                //print("\tleft is NULL\n");
                return rightBranch;
            }else if(base->right == NULL){
                Node* leftBranch = replace(base, base->left);
                delete(base);
                //print("\tright is NULL\n");
                return leftBranch;
            }else{
                //print("\thave two children\n");
                //print("successor is ");
                Node* successor = findSuccessor(base);
                //printNode(successor);
                base->value = successor->value;
                base->cnt = successor->cnt;
                successor->cnt = 1;
                base->right = remove(base->right, successor->value);
            }
        }
    }
    update(base, base);
    //print("remove done\n");
    return base;
}

void Tree::rotate(Node* n){
    //print("rotate\t... ");
    //printNode(n);
    assert(n->parent != NULL);
    Node* p = n->parent;
    if(isLeft(n)){
        replace(p->left, n->right);
        n->right = p;
    }else if(isRight(n)){
        replace(p->right, n->left);
        n->left = p;
    }
    replace(p, n);
    p->parent = n;
    update(n, p);
    //print("done\n");
}

void Tree::splay(Node* n){
    //print("splay\t... ");
    //printNode(n);
    while(n->parent){
        //print(". ");
        Node* p = n->parent;
        Node* g = p->parent;
        if(g != NULL){
            if((isLeft(n) && isLeft(p)) || (isRight(n) && isRight(p))) {
                //print("same direction ");
                rotate(p);
            }else{
                //print("diff direction ");
                rotate(n);
            }
        }
        rotate(n);
    }
    root = n;
    //print("done\n");
    //print("root is ");
    //printNode(root);
}

Node* Tree::findMid(){
    //print("findMid\t... ");
    Node* base = root;
    int l = getSize(base->left);
    int r = getSize(base->right);
    while(base != NULL){
        int cnt = base->cnt;
        if(abs(r-l) < cnt || l+cnt == r){
            break;
        }
        if(l < r){
            base = base->right;
            l += getSize(base->left) + cnt;
            r -= getSize(base->left) + base->cnt;
        }else{
            base = base->left;
            r += getSize(base->right) + cnt;
            l -= getSize(base->right) + base->cnt;
        }
    }
    //print("done\n");
    return base;
}

const int MAX_N = 250005;
const int MAX_K = 5005;

int main(){
    int N, K, arr[MAX_K];
    memset(arr, 0, sizeof(int)*MAX_K);
    LL sum = 0;
    scanf("%d %d", &N, &K);
    Tree tree = Tree();
    for(int i=0; i<N; ++i){
        int j = i % K;
        //printf("get %dth tinput: ", i+1);
        scanf("%d", & arr[j]);
        //printf("%d\n", arr[j]);
        //for(int k=0; k<K; ++k) if(DEBUG) printf("%d ", arr[k]);
        //print("\n");
        //if(DEBUG) printf("%dth ", i+1);
        tree.insert(arr[j]);
        if(i >= K-1){
            Node* mid = tree.findMid();
            //print("\tmid: "); printNode(mid);
            sum += mid->value;
            //if(DEBUG) printf("sum: %lld\n", sum);
            tree.splay(mid);
            tree.remove(tree.root, arr[(i-(K-1)) % K]);
            //print("root is ");
            //printNode(tree.root);
        }
    }
    printf("%lld\n", sum);
}
