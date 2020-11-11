/*
 * solution.cpp
 * Copyright (C) 2017 Sungmin <smoh2044@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

struct Ant {
    int a;
    bool isLeft;
    int t;

    Ant(int a, int t){
        this->a = a;
        this->t = t;
        this->isLeft = a < 0;
    }

    bool operator<(const Ant& b) const{
        if(t == b.t){
            return a < b.a;
        }
        return t < b.t;
    }
};

int main(){
    int t;
    scanf("%d", &t);

    while(t--){
        int n, l, k;
        scanf("%d %d %d", &n, &l, &k);

        vector<Ant> ants;
        vector<int> b;

        for(int i=0; i<n; ++i){
            int p, a, t;
            scanf("%d %d", &p, &a);
            if(a < 0){
                t = p + 1;
            }else{
                t = l - p + 1;
            }
            ants.push_back(Ant(a, t));
            b.push_back(a);
        }

        int i = 0;
        for(auto& ant : ants){
            if(ant.isLeft){
                ant.a = b[i++];
            }
        }
        for(auto& ant : ants){
            if(!ant.isLeft){
                ant.a = b[i++];
            }
        }

        sort(ants.begin(), ants.end());

        printf("%d\n", ants[k-1].a);

    }

    return 0;
}
