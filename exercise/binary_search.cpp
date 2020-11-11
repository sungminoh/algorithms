#include <iostream>
#include <vector>

using namespace std;

int binary_search(const vector<int> &A, int x){
    int n = A.size();
    int l = -1, h = n;

    while(l + 1 < h){
        int m = (l + h) / 2;
        if(A[m] < x){
            l = m;
        }else{
            h = m;
        }
    }

    return h;
}

int main(){
    return 0;
}
