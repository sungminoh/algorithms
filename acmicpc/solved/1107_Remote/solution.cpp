/* solution.cpp
 * Copyright (C) 2017 Sungmin <smoh2044@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */

#include <iostream>
#include <cmath>
#include <set>
#include <vector>

using namespace std;

int ans, num;

vector<int> num2Seq(int n){
    vector<int> sequence;
    if(n == 0){
        sequence.push_back(0);
        return sequence;
    }
    while(n){
        int d = n % 10;
        sequence.push_back(d);
        n /= 10;
    }
    return sequence;
}

int getLength(int n){
    if(n == 0){
        return 1;
    }
    int i = 0;
    for(i=0; n; ++i){
        n /= 10;
    }
    return i;
}

int getLowerBound(int d, set<int> &s){
    auto it = s.lower_bound(d);
    if(it == s.begin()){
        return -1;
    }
    return *(--it);
}

int getUpperBound(int d, set<int> &s){
    auto it = s.upper_bound(d);
    if(it == s.end()){
        return -1;
    }
    return *it;
}


void genCandidates(set<int> &c, set<int> &s, int n, int l, int i){
    if(i == l){
        int cnt = l + abs(num - n);
        if(cnt < ans){
            ans = cnt;
        }
        //c.insert(n);
        return;
    }
    n *= 10;
    for(auto it=s.begin(); it!=s.end(); ++it){
        genCandidates(c, s, n + (*it), l, i+1);
    }
}

void printSet(set<int> &s){
    for(auto it=s.begin(); it!=s.end(); ++it){
        printf("%d\n", *it);
    }
}

int getAnswer(int n, set<int> s){
    ans = abs(n - 100);
    num = n;

    set<int> c;

    int len = getLength(n)-1;
    for(int i=0; i<=2; ++i){
        for(auto it=s.begin(); it!=s.end(); ++it){
            if(len+i == 0 || (*it == 0 && len+i > 1)) continue;
            //printf("len+i: %d, *it: %d\n", len+i, *it);
            genCandidates(c, s, *it, len+i, 1);
        }
    }

    //printSet(c);

    //int l = getLowerBound(n, c);
    //int u = getUpperBound(n, c);
    //printf("l: %d, u: %d\n", l, u);

    //if(l >= 0){
        //ans = min(ans, getLength(l) + (n - l));
    //}
    //if(u >= 0){
        //ans = min(ans, getLength(u) + (u - n));
    //}

    return ans;
}


int main(){
    int n, m;
    scanf("%d %d", &n, &m);
    set<int> buttons;
    for(int i=0; i<10; ++i){
        buttons.insert(i);
    }
    while(m--){
        int button;
        scanf("%d", &button);
        buttons.erase(button);
    }
    printf("%d\n", getAnswer(n, buttons));

    return 0;
}
