/*
 * solution.cpp
 * Copyright (C) 2017 Sungmin <smoh2044@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */

#include <iostream>

using namespace std;


class Solution {
    public:
        int lengthOfLastWord(string s) {
            int n = s.size();
            int j=n-1;
            while(s[j] == ' '){
                j--;
            }
            int i;
            for(i=j; i>=0; --i){
                if(s[i] == ' ') break;
            }
            return j-i;
        }
};

int main(){
    string s;
    getline(cin, s);
    cout << Solution().lengthOfLastWord(s);

    return 0;
}
