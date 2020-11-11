#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    int n;
    int price[1000][3];
    int memo[1000][3];

    scanf("%d", &n);
    for(int i=0; i<n; ++i){
        scanf("%d %d %d", &price[i][0], &price[i][1], &price[i][2]);
    }

    for(int i=1; i<n; ++i){
        price[i][0] += min(price[i-1][1], price[i-1][2]);
        price[i][1] += min(price[i-1][0], price[i-1][2]);
        price[i][2] += min(price[i-1][1], price[i-1][0]);
    }

    printf("%d\n", *min_element(price[n-1], price[n-1]+3));

    return 0;
}
