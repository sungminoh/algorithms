#include <iostream>
#include <cmath>

using namespace std;

double getLength(int x, int y){
    return sqrt((x * x) + (y * y));
}

double solve(int x[], int y[], int N){
    int xSum = 0, ySum = 0;
    for(int i=0; i<N/2; ++i){
        xSum += x[i];
        ySum += y[i];
    }
    for(int i=N/2; i<N; ++i){
        xSum -= x[i];
        ySum -= y[i];
    }
    int minLength = getLength(xSum, ySum);

    for(int i=N/2-1; i>=0; --i){
        xSum -= x[i]*2;
        ySum -= y[i]*2;
        for(int j=N/2; j<N; ++j){
        }
    }
}

int main(void){
    int T, N, x[20], y[20];
    cin >> T;
    for(int t=0; t<T; ++t){
        cin >> N;
        for(int n=0; n<N; ++n){
            cin >> x[n];
            cin >> y[n];
        }
        printf("%.6lf\n", solve(x, y, N));
    }


}
