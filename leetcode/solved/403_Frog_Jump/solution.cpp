/*
 * solution.cpp
 * Copyright (C) 2018 sungmin <smoh2044@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */


#include <bits/stdc++.h>


using namespace std;


class Solution {
public:
    bool canCross(vector<int>& stones) {
        int size = stones.size();
        unordered_set<int> road;
        for(auto stone=stones.begin(); stone!=stones.end(); ++stone)
            road.insert(*stone);

        unordered_map<int, set<int> > buckets;
        for(auto stone=stones.begin(); stone!=stones.end(); ++stone)
            buckets[*stone] = set<int>();

        buckets[0].insert(1);
        for(auto stone=stones.begin(); stone!=stones.end(); ++stone){
            set<int> bucket = buckets[*stone];
            for(auto jump=bucket.begin(); jump!=bucket.end(); ++jump){
                if(*jump == 0) continue;
                int pos = *stone + *jump;
                if(pos == stones[size-1]){
                    cout << *stone << " + " << *jump  << endl;
                    return true;
                }
                if(road.find(pos) != road.end()){
                    buckets[pos].insert((*jump)-1);
                    buckets[pos].insert(*jump);
                    buckets[pos].insert((*jump)+1);
                }
            }
        }
        return false;
    }
};


vector<int> getInput(){
    string s;
    getline(cin, s);
    stringstream ss(s);
    vector<int> stones;
    int n;
    while(ss >> n)
        stones.push_back(n);
    return stones;
}


int main(){
    vector<int> v = getInput();
    cout << Solution().canCross(v) << endl;

    return 0;
}
