#include <iostream>
#include <vector>

using namespace std;

typedef long long LL;

LL init[10] = {1, 1, 1, 2, 2, 3, 4, 5, 7, 9};
vector<LL> s(10);
int m = 10;

LL padovan(int n){
    if(m >= n){
        return s[n-1];
    }

    for(int i=m; i<n; ++i){
        s.push_back(s[i-5] + s[i-1]);
    }

    return s[n-1];
}

int main(){
    int t;
    scanf("%d", &t);

    // inititialize
    for(int i=0; i<10; ++i){
        s[i] = init[i];
    }

    while(t--){
        int n;
        scanf("%d", &n);
        printf("%lld\n", padovan(n));
        if(n > m){
            m = n;
        }
    }
    return 0;
}
