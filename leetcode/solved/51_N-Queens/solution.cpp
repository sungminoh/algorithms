/*
 * solution.cpp
 * Copyright (C) 2017 Sungmin <smoh2044@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */

#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

class Solution {
    public:
        void printAll(vector<int>& q, unordered_set<int>& d, unordered_set<int>& s){
            cout << "q: ";
            for(auto e : q) cout << e << " ";
            cout << endl;
            cout << "d: ";
            for(auto e : d) cout << e << " ";
            cout << endl;
            cout << "s: ";
            for(auto e : s) cout << e << " ";
            cout << endl;
        }
        bool isin(int& i, int& j, vector<int>& q, unordered_set<int>& d, unordered_set<int>& s){
            bool ret = false;
            for(auto p : q){
                if(p == j){
                    ret = true;
                    break;
                }
            }
            if(d.find(i-j) != d.end()) ret = true;
            if(s.find(i+j) != s.end()) ret = true;
            return ret;
        }
        void dfs(vector<int>& q, unordered_set<int>& d, unordered_set<int>& s, int& n, vector<vector<string> >& ret){
            int qn = q.size();
            if(qn == n){
                //printAll(q, d, s);
                vector<string> sol;
                for(auto i : q){
                    string s = string(i, '.') + "Q" + string(n-i-1, '.');
                    sol.push_back(s);
                }
                ret.push_back(sol);
                return;
            }
            for(int i=0; i<n; ++i){
                if(isin(qn, i, q, d, s)) continue;
                q.push_back(i);
                d.insert(qn-i);
                s.insert(qn+i);
                dfs(q, d, s, n, ret);
                q.pop_back();
                d.erase(qn-i);
                s.erase(qn+i);
            }
        }
        vector<vector<string>> solveNQueens(int n) {
            vector<vector<string> > ret;
            vector<int> q;
            unordered_set<int> d;
            unordered_set<int> s;
            dfs(q, d, s, n, ret);
            return ret;
        }
};


int main(){
    ios_base::sync_with_stdio(false);
    int n;
    cin >> n;
    vector<vector<string> > sols = Solution().solveNQueens(n);
    for(auto sol: sols){
        for(auto l : sol){
            cout << l << endl;
        }
        cout << endl;
    }
    return 0;
}
