#include <iostream>
#include <vector>

using namespace std;

int getMaxSize(vector<int> &h, int l, int r){
    if(l == r){
        return h[l];
    }else{
        int m = (l + r) / 2;
        int ret = max(getMaxSize(h, l, m), getMaxSize(h, m+1, r));
        int i = m, j = m+1;
        int height = min(h[i], h[j]);
        ret = max(ret, height*2);
        while(l < i || j < r){
            if(j < r && (i == l || h[i-1] < h[j+1])){
                height = min(height, h[++j]);
            }else{
                height = min(height, h[--i]);
            }
            ret = max(ret, height*(j-i+1));
        }
        return ret;
    }
}

int main(){
    int c;
    scanf("%d", &c);
    while(c--){
        int n;
        scanf("%d", &n);
        vector<int> h(n);
        for(int i=0; i<n; ++i){
            scanf("%d", &h[i]);
        }
        printf("%d\n", getMaxSize(h, 0, n-1));
    }
    return 0;
}
