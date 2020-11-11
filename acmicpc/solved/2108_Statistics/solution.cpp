#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
#include <cmath>


typedef long long LL;

using namespace std;

map<int, int> m;


const int MAX_N = 500005;
const int MAX_V = 4005;


int main(){
    int N, v, l=4005, h=-4005;
    LL sum = 0;
    scanf("%d", &N);
    for(int i=0; i<N; ++i){
        scanf("%d", &v);
        // for average
        sum += v;
        // for mode and median
        int cnt = 1;
        if(m.find(v) != m.end()){
            m[v] ++;
        }else{
            m.insert(make_pair(v, cnt));
        }
        // for range upper bound
        if(v > h){
            h = v;
        }
        // for range lower bound
        if(v < l){
            l = v;
        }
    }
    // find average
    int avg = (int) round((double) sum / N);
    // find median and mode
    vector<int> modes;
    LL acc = 0;
    int max_freq = 0;
    int mid = 987654321;
    map<int, int>::iterator iter;
    //printf("map\n");
    //for(iter=m.begin(); iter!=m.end(); ++iter){
        //printf("val: %d, cnt: %d\n", iter->first, iter->second);
    //}
    for(iter=m.begin(); iter!=m.end(); ++iter){
        int val = iter->first;
        int freq = iter->second;
        // find median
        acc += freq;
        if(mid > 40000 && acc >= round(N/2.0)){
            //printf("find mid: %d", val);
            mid = val;
        }
        // find mode
        if(freq > max_freq){
            max_freq = freq;
            modes.clear();
            modes.push_back(val);
        }else if(freq == max_freq){
            modes.push_back(val);
        }
    }
    sort(modes.begin(), modes.end());
    //for(vector<int>::iterator it=modes.begin(); it!=modes.end(); ++it){
        //printf("%d\t", *it);
    //}
    //printf("\n");
    int mode = modes.size() > 1 ? modes[1] : modes[0];
    // find range
    int range = h - l;

    //printf("avg: %d\nmid: %d\nmode: %d\nrange: %d\n", avg, mid, mode, range);
    printf("%d\n%d\n%d\n%d", avg, mid, mode, range);
}
