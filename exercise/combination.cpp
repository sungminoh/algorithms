#include <iostream>
#include <vector>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef vector<LL> BLL;
typedef vector<vector<LL> > matrix;

LL getOrDefault(vector<LL> v, int i, int d){
    if(i >= v.size()){
        return d;
    }else{
        return v[i];
    }
}


BLL operator + (const BLL &a, const BLL &b){
    BLL ret;
    LL MAX = 1000000000000000000;
    int as = a.size(), bs = b.size();
    int m = max(as, bs);
    int c = 0;
    for(int i=0; i<m; ++i){
        LL sum = getOrDefault(a, i, 0) + getOrDefault(b, i, 0) + c;
        c = sum / MAX;
        LL d = sum % MAX;
        ret.push_back(d);
    }
    if(c > 0)
        ret.push_back(c);
    return ret;
}

LL combinationMemo(int n, int m, matrix memo){
    if(n == m || m == 0){
        return 1;
    }
    if(memo[n][m] == 0){
        memo[n][m] = combinationMemo(n-1, m-1, memo) + combinationMemo(n-1, m, memo);
    }
    return memo[n][m];
}

LL combinationNaive(int n, int m){
    if(n == m || m == 0){
        return 1;
    }
    return combinationNaive(n-1, m-1) + combinationNaive(n-1, m);
}

BLL combinationDynamic(int n, int m){
    if(n == m || m == 0){
        return BLL(1, 1);
    }
    vector<BLL> memo[2];
    memo[0] = vector<BLL>(n);
    memo[1] = vector<BLL>(n);
    memo[0][0] = memo[1][0] = BLL(1, 1);
    for(int i=1; i<=n-1; ++i){
        memo[i%2][i] = BLL(1, 1);
        for(int j=1; j<=i; ++j){
            memo[i%2][j] = memo[(i+1)%2][j-1] + memo[(i+1)%2][j];
        }
    }
    return memo[(n+1)%2][m-1] + memo[(n+1)%2][m];
}


int main(){
    int n, m;
    scanf("%d %d", &n, &m);

    //matrix memo(n+1);
    //for(int i=1; i<=n; ++i){
        //memo[i] = vector<LL>(i);
    //}
    //LL ans = combinationMemo(n, m, memo);

    //LL ans = combinationNaive(n, m);

    //for(int i=0; i<=n; ++i){
        //for(int j=0; j<=i; ++j){
            //LL ans = combinationDynamic(i, j);
            //printf("%ll ", ans);
        //}
        //printf("\n");
    //}

    BLL ans = combinationDynamic(n, m);
    for(auto i = ans.rbegin(); i != ans.rend(); ++i){
        printf("%lld", *i);
    }
    printf("\n");

    return 0;
}
