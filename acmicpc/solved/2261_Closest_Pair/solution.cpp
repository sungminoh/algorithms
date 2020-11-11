/*
 * solution.cpp
 * Copyright (C) 2017 Sungmin <smoh2044@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */

#include <iostream>
#include <map>
#include <vector>
#include <tuple>
#include <unordered_set>
#include <cmath>

using namespace std;

typedef unordered_set<int> set;
typedef map<int, set> Map;
int INF = 800000001;

Map getInputs(){
    int n;
    bool duplicates = false;
    scanf("%d", &n);
    Map points;
    for(int i=0; i<n; ++i){
        int x, y;
        scanf("%d %d", &x, &y);
        if(points.find(x) == points.end()){
            set ys;
            points.insert(make_pair(x, ys));
        }
        auto result = points.at(x).insert(y);
        if(result.second == false){
            duplicates = true;
        }
    }
    if(duplicates){
        printf("0\n");
        exit(0);
    }
    return points;
}

int findMinDist(Map::iterator l, Map::iterator r, int &dist){
    //cout << "l: " << l->first << ", r: " << r->first << ", dist: " << dist << endl;
    int x = r->first;
    set ys = r->second;
    for(set::iterator y1 = ys.begin(); y1 != ys.end(); ++y1){
        for(set::iterator y2 = next(y1); y2 != ys.end(); ++y2){
            if(y1 == y2) break;
            int newDist = pow(*y2 - *y1, 2);
            if(newDist < dist){
                dist = newDist;
            }
        }
    }
    if(l == r) return dist;
    for(Map::iterator k = prev(r); ; --k){
        int a = k->first;
        set bs = k->second;
        int xSquare = pow(a-x, 2);
        if(xSquare >= dist) break;
        for(set::iterator y = ys.begin(); y != ys.end(); ++y){
            for(set::iterator b = bs.begin(); b != bs.end(); ++b){
                int newDist = pow(*y-*b, 2) + xSquare;
                if(newDist < dist){
                    dist = newDist;
                }
            }
        }
        if(k == l) break;
    }
    return dist;
}


int findMinDistPair(Map points){
    int dist = INF;
    for(Map::iterator point = points.begin(); point != points.end(); ++point){
        int x = point->first;
        set ys = point->second;
        Map::iterator bound = points.upper_bound(x - ceil(sqrt(dist)));
        findMinDist(bound, point, dist);
    }
    return dist;
}


int main(){
    Map points = getInputs();
    int dist = findMinDistPair(points);
    printf("%d\n", dist);
    return 0;
}
