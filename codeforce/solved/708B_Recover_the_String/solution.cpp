#include <bits/stdc++.h>

using namespace std;

int a00, a01, a10, a11;

int getNumberOfZerosOrOnes(int a){
    int root = sqrt(a*2);
    if(root*(root+1) == a*2){
        return root+1;
    };
    return -1;
}

void solve(){
    int numberOfZeros = getNumberOfZerosOrOnes(a00);
    int numberOfOnes = getNumberOfZerosOrOnes(a11);
    if(numberOfOnes < 0 || numberOfZeros < 0){
        cout << "Impossible";
        return;
    }
    if(a01 == 0 && a10 == 0){
        if(a00 == 0) numberOfZeros = 0;
        else if(a11 == 0) numberOfOnes = 0;
    }
    if(numberOfZeros * numberOfOnes !=  a01 + a10){
        cout << "Impossible";
        return;
    }
    int numberOfDigits = numberOfOnes + numberOfZeros;
    vector<int> sequence;
    sequence.reserve(numberOfDigits);
    for(int i=0; i<numberOfOnes; ++i){
        sequence.push_back(1);
    }
    for(int i=numberOfOnes; i<numberOfDigits; ++i){
        sequence.push_back(0);
    }
    int i = 0;
    int j = numberOfOnes;
    for(int numberOfa01=0; numberOfa01 < a01; numberOfa01+=numberOfOnes){
        if(a01 - numberOfa01 >= numberOfOnes){
            swap(sequence[i++], sequence[j++]);
        }else{
            swap(sequence[j-(a01-numberOfa01)], sequence[j]);
        }
    }
    copy(sequence.begin(), sequence.end(), ostream_iterator<int>(cout, ""));
}

int main(){
    scanf("%d %d %d %d", &a00, &a01, &a10, &a11);
    solve();
}
