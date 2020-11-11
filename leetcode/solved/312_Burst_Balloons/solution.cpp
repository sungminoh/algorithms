/*
 * solution.cpp
 * Copyright (C) 2017 Sungmin <smoh2044@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */

#include <iostream>
#include <vector>

using namespace std;
typedef vector<vector<int> > Mat;

vector<int> getInput(){
    char c;
    vector<int> ret;
    while(cin.get(c) && c != '\n'){
        if(c == ' ') continue;
        ret.push_back(c - '0');
    }
    return ret;
}

void printVec(vector<int> v){
    for(auto e : v) printf("%d ", e);
    printf("\n");
}

void printMat(Mat m){
    for(auto v : m) printVec(v);
}

class Solution {
    public:
        int maxCoins(vector<int>& nums){
            /* Nothing but the numbers of multiplication in matrix chain.
             * a1 a2 a3 a4 ->
             * (1, a1)*(a1, a2)*(a2, a3)*(a3, a4)*(a4, 1)
             */
            int size = nums.size();
            nums.insert(nums.begin(), 1);
            nums.push_back(1);
            Mat mat(size+1, vector<int>(size+1, 0));
            return maxCoinsDynamic(nums, 0, size, mat, 0);
        }

        int maxCoinsDynamic(vector<int>& nums, int i, int j, Mat& memo, int depth){
            if(i == j) return 0;
            if(memo[i][j]) return memo[i][j];
            int m = -1;
            int l, r, c, cnt, k_;
            for(int k=i; k<j; ++k){
                l = maxCoinsDynamic(nums, i, k, memo, depth+1);
                r = maxCoinsDynamic(nums, k+1, j, memo, depth+1);
                c = nums[i]*nums[k+1]*nums[j+1];
                cnt = l + r + c;
                if(cnt > m){
                    k_ = k;
                    m = cnt;
                }
            }
            memo[i][j] = m;
            return m;
        }


        int maxCoinsBrute(vector<int>& nums){
            int size = nums.size();
            int m = 0;
            for(int i=0; i<size; ++i){
                int n, n_;
                n = n_ = nums[i];
                if(i > 0) n *= nums[i-1];
                if(i < size-1) n *= nums[i+1];
                nums.erase(nums.begin() + i);
                n += maxCoinsBrute(nums);
                if(n > m) m = n;
                nums.insert(nums.begin() + i, n_);
            }
            return m;
        }
};

int main(){
    vector<int> v = getInput();
    int sol = Solution().maxCoins(v);
    printf("%d\n", sol);
    return 0;
}
