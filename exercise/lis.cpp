#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void update(const vector<int> &lst, vector<int> &c){
    int added = lst.back();
    if(c.size() == 0){
        c.push_back(added);
        return;
    }
    auto it =  upper_bound(c.begin(), c.end(), added);
    if(it == c.end() && c.back() < added){
        c.push_back(added);
    }else if(it == c.begin() || *(it-1) != added){
        *it = added;
    }
}

void printVec(const vector<int> &v){
    for(auto it=v.begin(); it<v.end(); ++it){
        printf("%d ", *it);
    }
    printf("\n");
}

int main(){
    int n;
    scanf("%d", &n);
    vector<int> lst;
    vector<int> c;
    for(int i=0; i<n; ++i){
        int v;
        scanf("%d", &v);
        lst.push_back(v);
        update(lst, c);
        //printVec(lst);
        //printVec(c);
    }
    printf("%d\n", (int) c.size());
    return 0;
}
