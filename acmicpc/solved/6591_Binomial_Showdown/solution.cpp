#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

typedef long long LL;
typedef vector<LL> BLL;
const int MAX = 100000000;

LL getOrDefault(const BLL &a, int idx, LL def){
    if(a.size() > idx){
        return a[idx];
    }
    return def;
}

BLL operator + (const BLL &a, const BLL &b){
    BLL ret;
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


BLL operator * (const BLL &a, const LL &b){
    BLL ret;
    LL c = 0;
    for(auto it=a.begin(); it!=a.end(); ++it){
        LL mul = *it * b + c;
        c = mul / MAX;
        mul %= MAX;
        ret.push_back(mul);
    }
    if(c){
        ret.push_back(c);
    }
    return ret;
}



BLL operator / (const BLL &a, const LL &b){
    BLL ret;
    LL c = 0;
    for(auto it=a.rbegin(); it!=a.rend(); ++it){
        LL val = *it + (c * MAX);
        c = val % b;
        val /= b;
        if(val)
            ret.push_back(val);
    }
    reverse(ret.begin(), ret.end());
    return ret;
}

BLL combinationLarge(int n, int m){
    if(m > n-m){
        m = n-m;
    }
    if(m == 0){
        return BLL(1, 1);
    }
    if(m == 1){
        return BLL(1, n);
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

LL combinationDynamic(LL n, LL m){
    if(m > n-m){
        m = n-m;
    }
    if(m == 0){
        return 1;
    }
    if(m == 1){
        return n;
    }
    vector<LL> numerators(m);
    vector<LL> denominators;
    for(LL i=0; i<m; ++i){
        numerators[i] = (LL) n-i;
    }
    for(LL d=2; d<=m; ++d){
        for(LL i=0; i<m; ++i){
            if(numerators[i] % d == 0){
                numerators[i] /= d;
                break;
            }
            if(i == m-1){
                denominators.push_back(d);
            }
        }
    }

    BLL bll = BLL(1, 1);
    for(LL i=0; i<m; ++i){
        bll = bll * numerators[i];
    }
    for(auto it=denominators.begin(); it!=denominators.end(); ++it){
        bll = bll / *it;
    }
    LL ret = 0;
    LL c = 1;
    for(auto it=bll.begin(); it!=bll.end(); ++it){
        ret += (*it * c);
        c *= MAX;
    }
    return ret;
}



int main(){
    LL n, m;
    while(true){
        scanf("%lld %lld", &n, &m);
        if(n == 0 && m == 0)
            break;

        LL ans = combinationDynamic(n, m);
        printf("%lld\n", ans);
    }


    //for(n=0; n<100; ++n){
        //for(m=0; m<=n; ++m){
            //LL ans = combinationDynamic(n, m);

            //BLL ansLarge = combinationLarge(n, m);
            //LL lrg = 0;
            //int s = ansLarge.size();
            //for(int i=0; i<s; ++i){
                //lrg += pow(MAX, i) * ansLarge[i];
            //}

            //if(lrg < MAX && ans != lrg){
                //printf("ans %lld C %lld: %lld\n", n, m, ans);
                //printf("lng %lld C %lld: %lld\n", n, m, lrg);
            //}
        //}
    //}

    return 0;
}
