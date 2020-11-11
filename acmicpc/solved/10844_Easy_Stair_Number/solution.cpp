#include <iostream>
#include <vector>

typedef unsigned long long LL;
const int MOD = 1000000000;

using namespace std;

void print_vector(vector<LL> &v){
    for(vector<LL>::iterator it=v.begin(); it!=v.end(); ++it){
        printf("%llu ", *it);
    }
}

int main(){
    int n;
    scanf("%d", &n);

    vector<LL> cnts[2];

    // initialize
    cnts[1].push_back(0);
    for(int i=1; i<=9; ++i){
        cnts[1].push_back(1);
    }

    for(int i=2; i<=n; ++i){
        vector<LL> previous = cnts[(i-1)%2];
        vector<LL> current = cnts[i%2];
        current.push_back(previous[1]);
        for(int i=1; i<=8; ++i){
            current.push_back((previous[i-1] + previous[i+1]) % MOD);
        }
        current.push_back(previous[8]);
        cnts[i%2] = current;
        cnts[(i-1)%2].clear();
    }


    LL sum = 0;
    for(int i=0; i<=9; ++i){
        sum += cnts[n%2][i];
    }
    printf("%llu\n", sum % MOD);

    return 0;
}
