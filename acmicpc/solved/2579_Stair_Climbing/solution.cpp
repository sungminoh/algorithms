#include <iostream>

typedef long long LL;

using namespace std;

int main(){
    int n;
    scanf("%d", &n);

    int scores[300][2];
    // 0: stepping on the next stair is possible
    // 1: stepping on the next stair is not possible
    int v;
    scanf("%d", &v);
    scores[0][0] = scores[0][1] = v;
    scanf("%d", &v);
    scores[1][0] = v;
    scores[1][1] = v + scores[0][0];
    for(int i=2; i<n; ++i){
        scanf("%d", &v);
        scores[i][0] = v + max(scores[i-2][0], scores[i-2][1]);
        scores[i][1] = v + scores[i-1][0];
    }

    printf("%d\n", max(scores[n-1][0], scores[n-1][1]));


    return 0;
}
