#include <iostream>
#include <vector>


using namespace std;

void print_vector(vector<int> &v){
    for(vector<int>::iterator it=v.begin(); it!=v.end(); ++it){
        printf("%d ", *it);
    }
}

int main(){
    int n;
    scanf("%d", &n);

    vector<int> numberOfSteps(n+1);
    numberOfSteps[1] = 1;
    for(int i=2; i<=n; ++i){
        numberOfSteps[i] = numberOfSteps[i-1] + 1;
        if(i % 3 == 0){
            numberOfSteps[i] = min(numberOfSteps[i], numberOfSteps[i/3] + 1);
        }
        if(i % 2 == 0){
            numberOfSteps[i] = min(numberOfSteps[i], numberOfSteps[i/2] + 1);
        }
    }

    printf("%d\n", numberOfSteps[n]-1);

    return 0;
}
