#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
    int n, v;
    scanf("%d", &n);
    vector<int> layers[2];
    scanf("%d", &v);
    layers[0].push_back(v);
    for(int i=1; i<n; ++i){
        vector<int> previous = layers[(i+1)%2];
        vector<int> current = layers[i%2];

        for(int j=0; j<=i; ++j){
            int v;
            scanf("%d", &v);
            current.push_back(v + (j == 0 ? previous[j] : j == i ? previous[j-1] : max(previous[j-1], previous[j])));
        }
        layers[i%2] = current;

        layers[(i+1)%2].clear();
    }

    vector<int> last = layers[(n-1)%2];
    printf("%d", *max_element(last.begin(), last.end()));

    return 0;
}
