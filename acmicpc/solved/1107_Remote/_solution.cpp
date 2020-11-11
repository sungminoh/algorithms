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

int INF = 987654321;

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

bool isValid(int n, set<int> &s){
    if(n == 0){
        return s.find(0) != s.end();
    }
    while(n){
        int d = n%10;
        if(s.find(d) == s.end()){
            return false;
        }
        n /= 10;
    }
    return true;
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

int getAnswer(int n, set<int> s){
    int direct = abs(n - 100);

    if(s.size() == 0){
        return direct;
    }

    int cnt = 0;
    vector<int> sequence = num2Seq(n);

    bool match = true;
    int i, d, m = 0;
    for(i=sequence.size()-1; i>=0; --i){
        d = sequence[i];
        if(s.find(d) == s.end()){
            match = false;
            break;
        }
        if(match){
            m += d * pow(10, i);
            cnt ++;
        }
    }
    if(!match){
        int mi = *(s.begin());
        int ma = *(s.rbegin());
        int l = getLowerBound(d, s);
        int u = getUpperBound(d, s);

        int ml = m, mu = m;
        //printf("m: %d, l: %d, u: %d\n", m, l, u);
        if(l < 0){
            ml -= pow(10, i+1);
            if(ml < 0){
                ml = -9 * pow(10, i);
            }
            ml += (ma * pow(10, i));
            mu += u*pow(10, i);
        }else if(u < 0){
            mu += pow(10, i+1);
            mu += (mi * pow(10, i));
            ml += l*pow(10, i);
        }else{
            ml += l*pow(10, i);
            mu += u*pow(10, i);
        }
        for(int j=i-1; j>=0; --j){
            ml += ma * pow(10, j);
            mu += mi * pow(10, j);
        }
        //printf("ml: %d\n", ml);
        //printf("mu: %d\n", mu);
        if(!isValid(ml, s)){
            ml = INF;
        }
        if(!isValid(mu, s)){
            mu = INF;
        }
        return min(direct, min(getLength(mu)+ abs(mu - n), getLength(ml) + abs(n - ml)));
    }else{
        //printf("direct: %d, cnt: %d\n", direct, cnt);
        return min(direct, cnt);
    }
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
