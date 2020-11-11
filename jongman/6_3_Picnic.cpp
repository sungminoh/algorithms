#include <iostream>
#include <vector>

using namespace std;


int countPairings(vector<vector<bool> > &areFriends, vector<bool> &taken){
    int n = taken.size();
    int i = -1;
    for(int k=0; k<n; ++k){
        if(!taken[k]){
            i = k;
            break;
        }
    }
    if(i == -1) return 1;
    int ret = 0;
    for(int j=i+1; j<n; ++j){
        if(!taken[i] && !taken[j] && areFriends[i][j]){
            taken[i] = taken[j] = true;
            ret += countPairings(areFriends, taken);
            taken[i] = taken[j] = false;
        }
    }
    return ret;
}

int main(){
    int t;
    scanf("%d", &t);
    while(t--){
        int n, m;
        scanf("%d %d", &n, &m);
        vector<vector<bool> > areFriends;
        areFriends.resize(n, vector<bool>(false));
        while(m--){
            int i, j;
            scanf("%d %d", &i, &j);
            areFriends[i][j] = areFriends[j][i] = true;
        }
        vector<bool> taken(n, false);

        printf("%d\n", countPairings(areFriends, taken));
    }

    return 0;
}
