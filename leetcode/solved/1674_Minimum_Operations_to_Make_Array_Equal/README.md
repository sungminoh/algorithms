### [1674. Minimum Operations to Make Array Equal](https://leetcode.com/problems/minimum-operations-to-make-array-equal/)

Medium

You have an array `` arr `` of length `` n `` where `` arr[i] = (2 * i) + 1 `` for all valid values of `` i `` (i.e. `` 0 <= i < n ``).

In one operation, you can select two indices `` x `` and `` y `` where `` 0 <= x, y < n `` and subtract `` 1 `` from `` arr[x] `` and add `` 1 `` to `` arr[y] `` (i.e. perform `` arr[x] -=1  ``and `` arr[y] += 1 ``). The goal is to make all the elements of the array __equal__. It is __guaranteed__ that all the elements of the array can be made equal using some operations.

Given an integer `` n ``, the length of the array. Return _the minimum number of operations_ needed to make all the elements of arr equal.

 

__Example 1:__

```
Input: n = 3
Output: 2
Explanation: arr = [1, 3, 5]
First operation choose x = 2 and y = 0, this leads arr to be [2, 3, 4]
In the second operation choose x = 2 and y = 0 again, thus arr = [3, 3, 3].
```

__Example 2:__

```
Input: n = 6
Output: 9
```

 

__Constraints:__

*   `` 1 <= n <= 10^4 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 59,525 | 48,092 | 80.8% |