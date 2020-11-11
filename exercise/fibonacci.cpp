#include <iostream>
#include <vector>

using namespace std;

typedef unsigned long long LL;
typedef vector<vector<LL> > matrix;

matrix operator * (const matrix &a, const matrix &b){
    int n = a.size();
    matrix c(n, vector<LL>(n));
    for(int i=0; i<n; ++i){
        for(int j=0; j<n; ++j){
            for(int k=0; k<n; ++k){
                c[i][j] += a[i][k] * b[k][j];
            }
            c[i][j] %= 1000000;
        }
    }
    return c;
}

LL getFibonacci_naive(int n){
    if(n <= 1){
        return n;
    }
    LL n1=1, n2=0, n0=1;
    for(int i=3; i<=n; ++i){
        n2 = n1;
        n1 = n0;
        n0 = n1 + n2;
    }
    return n0;
}

LL getFibonacci_matrix(LL n){
    matrix ans = {{1, 0}, {0, 1}};
    matrix a = {{1, 1}, {1, 0}};

    while(n > 0){
        if(n % 2 == 1){
            ans = ans * a;
        }
        a = a * a;
        n /= 2;
    }
    return ans[0][1];
}

int main(){
    LL n;
    scanf("%lld", &n);
    LL fibo = getFibonacci_matrix(n);
    printf("%llu\n", fibo % 1000000);
    return 0;
}
