#include <iostream>
#include <vector>

typedef long long LL;

using namespace std;

int main(){
    int n, pv, cv;
    scanf("%d", &n);

    vector<int> yes(n);
    vector<int> no(n);
    scanf("%d", &pv);
    yes[0] = pv;
    no[0] = 0;
    scanf("%d", &pv);
    yes[1] = yes[0] + pv;
    no[1] = yes[0];
    for(int i=2; i<n; ++i){
        scanf("%d", &cv);
        yes[i] = max(no[i-1], no[i-2] + pv) + cv;
        no[i] = max(no[i-1], yes[i-1]);
        pv = cv;
    }

    printf("%d\n", max(yes[n-1], no[n-1]));



    return 0;
}
