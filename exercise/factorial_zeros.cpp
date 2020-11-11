#include <iostream>

using namespace std;


int countFactors(int n, int p){
    int ret = 0;
    while(n % p == 0){
        ret++;
        n /= p;
    }
    return ret;
}


int main(){
    int n;
    scanf("%d", &n);

    int numberOfTwos= 0;
    int numberOfFives= 0;
    for(int i=2; i<=n; ++i){
        numberOfTwos += countFactors(i, 2);
        numberOfFives += countFactors(i, 5);
    }

    printf("%d\n", min(numberOfTwos, numberOfFives));
    return 0;
}
