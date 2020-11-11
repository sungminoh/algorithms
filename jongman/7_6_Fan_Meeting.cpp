#include <iostream>
#include <vector>

using namespace std;

vector<int> multiplyWitoutNormalize(const vector<int> &a, const vector<int> &b){
    int an = a.size();
    int bn = b.size();
    vector<int> c(an + bn + 1, 0);
    for(int i=0; i<bn; ++i){
        for(int j=0; j<an; ++j){
            c[i+j] += a[j]*b[i];
        }
    }
    while(c.size() > 1 && c.back() == 0){
        c.pop_back();
    }
    return c;
}

void addTo(vector<int> &a, vector<int> &b, int k){
    int an = a.size();
    int bn = b.size();
    int cn = max<int>(an, bn+k) + 1;
    for(int i=an; i<cn; ++i){
        a.push_back(0);
    }
    for(int i=0; i<bn; ++i){
        a[i+k] += b[i];
    }
    while(a.size() > 1 && a.back() == 0){
        a.pop_back();
    }
}

void subFrom(vector<int> &a, vector<int> &b){
    int an = a.size();
    int bn = b.size();

    for(int i=0; i<bn; ++i){
        a[i] -= b[i];
    }
    while(a.size() > 1 && a.back() == 0){
        a.pop_back();
    }
}

vector<int> karatsubaWithoutNormalize(const vector<int> &a, const vector<int> &b){
    int an = a.size();
    int bn = b.size();
    if(an < bn){
        return karatsubaWithoutNormalize(b, a);
    }
    if(an == 0 || bn == 0){
        return vector<int>();
    }
    if(an < 50){
        return multiplyWitoutNormalize(a, b);
    }

    int half = an / 2;
    int half_b = max<int>(half, bn);

    vector<int> a0(a.begin(), a.begin() + half);
    vector<int> a1(a.begin() + half, a.end());
    vector<int> b0(b.begin(), b.begin() + half_b);
    vector<int> b1(b.begin() + half_b, b.end());

    vector<int> z2 = karatsubaWithoutNormalize(a1, b1);
    vector<int> z0 = karatsubaWithoutNormalize(a0, b0);

    addTo(a0, a1, 0);
    addTo(b0, b1, 0);
    vector<int> z1 = karatsubaWithoutNormalize(a0, b0);
    subFrom(z1, z2);
    subFrom(z1, z0);

    vector<int> ret;
    addTo(ret, z0, 0);
    addTo(ret, z1, half);
    addTo(ret, z2, 2*half);

    return ret;
}


int getHugs(const string &members, const string &fans){
    int mn = members.size();
    int fn = fans.size();
    vector<int> a(mn), b(fn);
    for(int i=0; i<mn; ++i){
        a[i] = (members[mn-i-1] == 'M');
    }
    for(int i=0; i<fn; ++i){
        b[i] = (fans[i] == 'M');
    }
    vector<int> c = karatsubaWithoutNormalize(a, b);
    int cnt = 0;
    for(int i=mn-1; i<fn; ++i){
        if(c[i] == 0){
            cnt++;
        }
    }
    return cnt;
}


int main(){
    int c;
    scanf("%d", &c);
    while(c--){
        string members, fans;
        cin >> members;
        cin >> fans;
        printf("%d\n", getHugs(members, fans));
    }
    return 0;
}
