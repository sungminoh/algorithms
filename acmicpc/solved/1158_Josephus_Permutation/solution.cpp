#include <iostream>
#include <vector>

using namespace std;


void printJosephusPermutation(int n, int m){
    vector<int> l;
    for(int i=1; i<=n; ++i){
        l.push_back(i);
    }
    printf("<");
    for(int size = (int) l.size(), i = (m % size) - 1 >= 0 ? (m % size) - 1 : size - 1; ;){
        if(!--size){
            printf("%d>", l[i]);
            break;
        }
        printf("%d, ", l[i]);
        l.erase(l.begin() + i);
        i += m;
        i = (i % size) - 1 >= 0 ? (i % size) - 1 : size - 1;
    }
}

int main(){
    int N, M;
    scanf("%d %d", &N, &M);
    printJosephusPermutation(N, M);
    return 0;
}
