#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;


typedef vector<vector<int> > matrix;
const int MAX = 987654321;


void print_mat(matrix &m){
    for(matrix::iterator mit=m.begin()+1; mit!=m.end(); ++mit){
        for(vector<int>::iterator it=mit->begin()+1; it!=mit->end(); ++it){
            printf("%d\t", *it);
        }
        printf("\n");
    }
}


int main(){
    int t;
    scanf("%d", &t);
    while(t--){
        int n;
        scanf("%d", &n);

        matrix m, pivot;
        m.resize(n+1, vector<int>(n+1));
        pivot.resize(n+1, vector<int>(n+1));
        vector<int> sum(n+1);
        for(int i=1; i<=n; ++i){
            scanf("%d", &sum[i]);
            sum[i] += sum[i-1];
            m[i][i] = 0;
            pivot[i][i] = i;
        }

        for(int i=1; i<n; i++){
            for(int j=1; j<=n-i; ++j){
                int s = j;
                int e = i+j;
                m[s][e] = MAX;
                for(int k=pivot[s][e-1]; k<=pivot[s+1][e]; ++k){
                    int x = m[s][k-1] + m[k][e] + sum[e] - sum[s-1];
                    if(m[s][e] > x){
                        m[s][e] = x;
                        pivot[s][e] = k;
                    }
                }
            }
        }
        printf("%d\n", m[1][n]);
    }
    return 0;
}
