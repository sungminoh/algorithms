#include <iostream>
#include <complex>
#include <algorithm>
#include <vector>

using namespace std;


vector<int> findDeviders(int n){
    vector<int> ret;
    for(int i=2; i<=sqrt(n); ++i){
        if(n%i == 0){
            ret.push_back(i);
            if(i != sqrt(n)){
                ret.push_back(n/i);
            }
        }
    }
    ret.push_back(n);
    return ret;
}

int main(){
    int n, v, d;
    scanf("%d", &n);
    vector<int> numbers;
    while(n--){
        scanf("%d", &v);
        numbers.push_back(v);
    }

    int mi, ma;
    mi = ma = numbers[0];
    for(auto it=numbers.begin(); it!=numbers.end(); ++it){
        if(mi > *it){
            mi = *it;
        }
        if(ma < *it){
            ma = *it;
        }
    }

    vector<int> deviders = findDeviders(ma-mi);
    sort(deviders.begin(), deviders.end());

    for(auto dit=deviders.begin(); dit!=deviders.end(); ++dit){
        int i = *dit;
        int r = -1;
        int alive = true;
        for(auto it=numbers.begin(); it!=numbers.end(); ++it){
            int r_ = (*it) % i;
            if(r < 0){
                r = r_;
            }else if(r != r_){
                alive = false;
                break;
            }
        }
        if(alive){
            printf("%d\n", i);
        }
    }

    return 0;
}
