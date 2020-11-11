/*
 * solution.cpp
 * Copyright (C) 2017 Sungmin <smoh2044@gmail.com>
 *
 * Distributed under terms of the MIT license.
 */

#include <iostream>

using namespace std;


int solve(int n){
    /*
     * Let a[0] = k. (then, clearly a[k] >= 1)
     * Because there are k zeros, summation of n-1-k non-zeros must be n-k.
     * Therefore, all non-zero a[i] have to be 1 except one 2.
     *
     * 1. Let k > 2
     * If a[k] = 2, there must be one another k among non-zero a[i]. Contradiction.
     * Else a[k] = 1, a[1] = 2 because a[1] can not be 1.
     *   Meanwhile a[2] = 1 because a[1] is the only 2.
     *   If there exists i such that a[i] = 1, there must be j such that a[j] = i. Which can not happen.
     *   Therefore, for all the other i except 0, 1, 2, k, a[i] = 0.
     *   In the result, a[0] = n-4, a[1] = 2, a[2] = 1, a[n-4] = 1, a[i] = 0 for all the other i. (n-4 > 2)
     *
     * 2. Let k = 2
     * If a[k] = 2, there is no need to be one onother k in contrast with k > 2 case.
     *   But still, all the other non-zero a[i] must be 1.
     *   Let a[1] is non-zero, it also have to be 1. In this case, the only possible sequence is 2, 1, 2, 0, 0.
     *   If a[1] is zero, The only possible sequence is 2, 0, 2, 0.
     * If a[k] = 1, a[1] can not be 1.
     *   Because all non-zero have to be 1 except one 2, a[1] have to be 2.
     *   However, a[k] = a[2] = 1. Contradiction.
     *
     * 3. Let k = 1
     * a[0] = 1, a[k] = a[1] > 1.
     * So, a[k] = a[1] = 2, a[2] = 1, The sequence is 1, 2, 1, 0.
     *
     * In the summary,
     * If n > 6, there are the only possible seqeuence such that a[0] = n-4, a[1] = 2, a[2] = 1, a[n-4] = 1 and a[i] = 0 (o.w).
     * Other wise, only [2, 1, 2, 0, 0], [2, 0, 2, 0], [1, 2, 1, 0] are possible.
     */
    if(n <= 3 || n == 6)
        return 0;
    else if(n == 4)
        return 2;
    else
        return 1;
}

int main(){
    int t, n;
    scanf("%d", &t);
    while(t--){
        scanf("%d", &n);
        printf("%d\n", solve(n));
    }
    return 0;
}
