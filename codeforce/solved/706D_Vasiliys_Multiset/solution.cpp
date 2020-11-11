#include <bits/stdc++.h>
#define loop(x, n) for(int x=0; x<n; ++x)

using namespace std;

int q, x, ans, oneHot;
char op;
multiset<int> pool;

void printBit(int n){
    stringstream st;
    loop(x, 32){
        st << (n & 1);
        n = n >> 1;
    }
    string s = st.str();
    reverse(s.begin(), s.end());
    cout << s << endl;
}

int main(){
    pool.insert(0);
    cin >> q;
    loop(i, q){
        cin >> op >> x;
        if(op == '+') pool.insert(x);
        else if(op == '-') pool.erase(pool.find(x));
        else if(op == '?'){
            ans = 0;
            oneHot = 1 << 30;
            while(oneHot >= 1){
                ans |= ~x & oneHot; // check from largest bit which is good
                auto it = pool.lower_bound(ans); // find larger or equal
                if(it == pool.end() || *it >= ans + oneHot){
                    // if there is no such number or the number is out if it's place
                    ans ^= oneHot; // reset
                }
                oneHot >>= 1;
            }
            printf("%d\n", ans ^ x);
        }
    }
}
