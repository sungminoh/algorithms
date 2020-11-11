#include <iostream>
#include <vector>
#include <string>
#include <cmath>

using namespace std;


vector<int> str2IntVector(string s){
    int len = s.length();
    vector<int> ret(len);
    for(int i=0; i<len; ++i){
        ret[i] = s[len-i-1] - '0';
    }
    return ret;
}

void printIntVector(const vector<int> &c){
    for(auto it=c.rbegin(); it!=c.rend(); ++it){
        printf("%d", *it);
    }
}

void normalize(vector<int> &c){
    c.push_back(0);
    int cn = c.size();
    for(int i=0; i<cn; ++i){
        if(c[i] < 0){
            int borrow = (abs(c[i]) + 9) / 10;
            c[i+1] -= borrow;
            c[i] += borrow*10;
        }else{
            c[i+1] += c[i] / 10;
            c[i] %= 10;
        }
    }
    while(c.size() > 1 && c.back() == 0){
        c.pop_back();
    }
}

vector<int> multiply(const vector<int> &a, const vector<int> &b){
    int an = a.size();
    int bn = b.size();
    vector<int> c(an + bn, 0);
    for(int i=0; i<bn; ++i){
        for(int j=0; j<an; ++j){
            c[i+j] += a[j]*b[i];
        }
    }
    normalize(c);
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
    normalize(a);
}

void subFrom(vector<int> &a, vector<int> &b){
    int bn = b.size();
    for(int i=0; i<bn; ++i){
        a[i] -= b[i];
    }
    normalize(a);
}

vector<int> karatsuba(const vector<int> &a, const vector<int> &b){
    int an = a.size();
    int bn = b.size();
    if(an < bn){
        return karatsuba(b, a);
    }
    if(an == 0 || bn == 0){
        return vector<int>();
    }
    if(an <= 50){
        return multiply(a, b);
    }

    int half = an / 2;
    int half_b = min<int>(bn, half);
    vector<int> a0(a.begin(), a.begin() + half);
    vector<int> a1(a.begin() + half, a.end());
    vector<int> b0(b.begin(), b.begin() + half_b);
    vector<int> b1(b.begin() + half_b, b.end());

    vector<int> z2 = karatsuba(a1, b1);
    vector<int> z0 = karatsuba(a0, b0);

    addTo(a0, a1, 0);
    addTo(b0, b1, 0);

    vector<int> z1 = karatsuba(a0, b0);
    subFrom(z1, z0);
    subFrom(z1, z2);

    vector<int> ret;
    addTo(ret, z0, 0);
    addTo(ret, z1, half);
    addTo(ret, z2, 2*half);
    return ret;
}

int main(){
    string sa, sb;
    cin >> sa >> sb;
    vector<int> a = str2IntVector(sa);
    vector<int> b = str2IntVector(sb);
    printIntVector(karatsuba(a, b));
    printf("\n");
}
