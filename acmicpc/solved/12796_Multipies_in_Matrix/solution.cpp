/*
 * solution.cpp
 * Copyright (C) 2017 Sungmin <smoh2044@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */

#include <iostream>

using namespace std;


void solve(int k){
    printf("%d\n", 3);
    printf("%d 1 1 1\n", k+1);
}


int main(){
    /*
    * (m, 1) (1, 1) (1, 1) ... (1, 1) n times
    * MAX
    * m + m + ... + m n times -> nm
    * MIN
    * 1 + ... + 1 (n-1) times + m -> n-1 + m
    * nm - n - m + 1 = (n-1) * (m-1) = k
    * m = k+1, n = 2
    * (k+1, 1) (1, 1) (1, 1)
    */

    int k;
    scanf("%d", &k);
    solve(k);

    return 0;
}
