### [474. Ones and Zeroes](https://leetcode.com/problems/ones-and-zeroes/)

Medium

Given an array, `` strs ``, with strings consisting of only `` 0s `` and `` 1s ``. Also two integers `` m `` and `` n ``.

Now your task is to find the maximum number of strings that you can form with given __m__ `` 0s `` and __n__ `` 1s ``. Each `` 0 `` and `` 1 `` can be used at most __once__.

 

__Example 1:__

```
Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are "10","0001","1","0".
```

__Example 2:__

```
Input: strs = ["10","0","1"], m = 1, n = 1
Output: 2
<b>Explanation:</b> You could form "10", but then you'd have nothing left. Better form "0" and "1".
```

 

__Constraints:__

*   `` 1 <= strs.length <= 600 ``
*   `` 1 <= strs[i].length <= 100 ``
*   `` strs[i] `` consists only of digits '0' and '1'.
*   `` 1 <= m, n <= 100 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 104,982 | 44,346 | 42.2% |