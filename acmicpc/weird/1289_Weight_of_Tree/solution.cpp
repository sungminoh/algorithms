/*
 * solution.cpp
 * Copyright (C) 2017 Sungmin <smoh2044@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */

#include <iostream>
#include <vector>

using namespace std;
typedef vector<vector<pair<int, int> > > G;
typedef long long LL;
static LL MOD = 1000000007;

G getInput(){
    int n;
    scanf("%d", &n);
    if(n == 1){
        printf("0\n");
        exit(0);
    }
    G g(n+1, vector<pair<int, int> >());
    for(int i=0; i<n-1; ++i){
        int u, v, w;
        scanf("%d %d %d", &u, &v, &w);
        g[u].push_back({v, w});
        g[v].push_back({u, w});
    }
    return g;
}

void printG(G& g){
    int n = g.size()-1;
    for(int i=1; i<=n; ++i){
        printf("%d: ", i);
        for(auto e: g[i]){
            printf("(%d, %d) ", e.first, e.second);
        }
        printf("\n");
    }
}

void dfs1(G& g, vector<bool>& p, int v, LL w, LL& s){
    //printf("v: %d, w: %lld, s: %lld\n", v, w, s);
    for(auto ud : g[v]){
        int u = ud.first;
        if(p[u]) continue;
        p[u] = true;
        LL d = (LL) ud.second;
        LL w_ = (w * d) % MOD;
        s += w_;
        s %= MOD;
        dfs1(g, p, u, w_, s);
    }
}

LL solve1(G& g){
    int n = g.size()-1;
    vector<bool> p(n+1, false);
    LL s = 0;
    for(int i=1; i<=n; ++i){
        p.assign(n+1, false);
        p[i] = true;
        dfs1(g, p, i, 1, s);
    }
    return s/2;
}


int dfs2(G& g, vector<bool>& p, int v, LL w, LL& s){
    //printf("v: %d, w: %lld, s: %lld\n", v, w, s);
    LL fp = w;
    for(auto ud : g[v]){
        int u = ud.first;
        if(p[u]) continue;
        p[u] = true;
        LL d = (LL) ud.second;
        LL w_ = ((w+1)*d) % MOD;
        s = (s+w_) % MOD;
        //printf("from %d to %d, path: %lld, total: %lld\n", v, u, w_, s);
        LL sub = ((dfs2(g, p, u, w_, s)+1) * d) % MOD;
        w += sub;
    }
    return (w - fp);

}

int findLeaf(G& g){
    int n = g.size()-1;
    int i;
    for(i=1; i<=n; ++i){
        if(g[i].size() == 1){
            break;
        }
    }
    return i;
}

LL solve2(G& g){
    int n = g.size() - 1;
    int leaf = findLeaf(g);
    //printf("leaf: %d\n", leaf);
    vector<bool> p(n+1, false);
    p[leaf] = true;
    LL s=0;
    dfs2(g, p, leaf, 0, s);
    return s;
}

int findRoot(G& g){
    int n = g.size()-1;
    int i;
    for(i=1; i<=n; ++i){
        if(g[i].size() <= 2) break;
    }
    return i;
}


LL getWeight(G& g, vector<bool> p, LL& s, int r){
    int i=0;
    LL weight[2] = {1, 1};
    for(auto v : g[r]){
        int u = v.first;
        if(p[u]) continue;
        p[u] = true;
        LL fromU = getWeight(g, p, s, u);
        //printf("from %d: %lld\n", u, fromU);
        weight[i++] = (v.second * (fromU+1)) % MOD;
    }
    if(i == 0){
        return 0;
    }else if(i == 1){
        //printf("%d add to sum %lld, sum: %lld\n", r, weight[0], s);
        s += weight[0]; s %= MOD;
        return weight[0];
    }else{
        //printf("%d add to sum %lld, sum: %lld\n", r, weight[0]+weight[1]+(weight[0]*weight[1]), s);
        s += weight[0]; s %= MOD;
        s += weight[1]; s %= MOD;
        s += (weight[0] * weight[1]) % MOD; s %= MOD;
        return weight[0] + weight[1];
    }
}

LL solve3(G& g){
    int root = findRoot(g);
    //printf("root: %d\n", root);
    vector<bool> p(g.size(), false);
    p[root] = true;
    LL s = 0;
    getWeight(g, p, s, root);
    return s % MOD;
}


int main(){
    int t;
    scanf("%d", &t);
    //t = 1;
    while(t--){
        G g = getInput();
        //printG(g);
        //LL ans1 = solve1(g);
        LL ans2 = solve2(g);
        LL ans3 = solve3(g);
        //printf("%lld ", ans1);
        //printf(ans1 == ans2 ? "= " : "!= ");
        printf("%lld", ans2);
        printf(ans2 == ans3 ? "= " : "!= ");
        printf("%lld\n", ans3);
    }

    return 0;
}
