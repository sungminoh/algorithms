/*
 * solution.cpp
 * Copyright (C) 2018 sungmin <smoh2044@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */

#include <iostream>


using namespace std;


class Solution {
public:
    bool isPalindrome(int x) {
        if(x >= 0 && x < 10) return true;
        if(x < 0 || x%10 == 0) return false;
        int rev = 0;
        for(; x>rev; x/=10){
            rev = rev*10 + x%10;
            if(x == rev) break;
        }
        return rev == x;
    }
};


int main(){
    int x;
    cin >> x;
    cout << Solution().isPalindrome(x) << endl;

    return 0;
}
