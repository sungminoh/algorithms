/*
 * solution.cpp
 * Copyright (C) 2017 Sungmin <smoh2044@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */

#include <iostream>
#include <vector>

using namespace std;


class Solution {
    public:
        int maxSubArray(vector<int>& nums) {
            int until;
            int sofar;
            until = sofar = nums[0];
            int n = nums.size();
            for(int i=1; i<n; ++i){
                until = max(nums[i], until+nums[i]);
                sofar = max(until, sofar);
            }
            return sofar;
        }
};

int main(){
    ios_base::sync_with_stdio(false);
    int n;
    cin >> n;
    vector<int> nums(n);
    for(int i=0; i<n; ++i){
        cin >> nums[i];
    }
    int s = Solution().maxSubArray(nums);
    cout << s << endl;

    return 0;
}
