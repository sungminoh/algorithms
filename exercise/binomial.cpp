#include <iostream>
#include <vector>

using namespace std;

typedef unsigned long long LL;
typedef vector<vector<LL>> matrix;

LL binomialNaive(int n, int k){
    LL ret = 1;
    int m = n - k;
    while(n){
        ret *= n--;
    }
    while(k){
        ret /= k--;
    }
    while(m){
        ret /= m--;
    }
    return ret;
}

LL binomialRecursive(int n, int k){
    if(n <= 1 || n == k || k == 0){
        return 1;
    }
    return binomialRecursive(n-1, k-1) + binomialRecursive(n-1, k);
}

LL binomialDynamic(int N, int K){
    matrix m(N+1, vector<LL>(N+1));
    for(int i=0; i<=N; ++i){
        m[i][0] = 1;
        m[i][i] = 1;
    }
    for(int n=2; n<=N; ++n){
        for(int k=1; k<=N; ++k){
            m[n][k] = m[n-1][k-1] + m[n-1][k];
        }
    }
    return m[N][K];
}

matrix getInitialMemo(int N, int K){
    matrix m(N+1, vector<LL>(N+1));
    for(int i=0; i<=N; ++i){
        m[i][0] = 1;
        m[i][i] = 1;
    }
    return m;
}

LL binomialMemoization(int n, int k, matrix &m){
    if(m[n][k] <= 0){
        m[n][k] = binomialMemoization(n-1, k-1, m) + binomialMemoization(n-1, k, m);
    }
    return m[n][k];
}

LL binomialUsingFermatTheorem(int n, int k, LL m){
    /* This is applicable only if m is a prime number;
     *
     * Fermat's Theorem
     *     If m is a prime and a and m are relatively prime,
     *     then a^(m-1) = 1 (mod m).
     *     Therefore, a * a^(m-2) = 1 (mod m),
     *     a^(m-2) is inverse of a.
     *
     * What is modulo 1,000,000,007(prime) of N! / K!(N-K)!
     * This problem can be converted to what is modulo of A * B^(M-2)
     * when A = N!, B = K!(N-K)!
     * */

    LL a=1, b=1;
    for(int i=1; i<=n; ++i){
        a *= i;
        a %= m;
    }
    for(int i=1; i<=k; ++i){
        b *= i;
        b %= m;
    }
    for(int i=1; i<=n-k; ++i){
        b *= i;
        b %= m;
    }

    LL inv = 1;
    LL tmp = m-2;
    while(tmp > 0){
        if(tmp % 2 == 1){
            inv *= b;
            inv %= m;
        }
        b *= b;
        b %= m;
        tmp /= 2;
    }
    return (a * inv) % m;
}


int main(){
    int n, k;
    scanf("%d %d", &n, &k);

    printf("%llu\n", binomialUsingFermatTheorem(n, k, 1000000007LL));
    return 0;
}
