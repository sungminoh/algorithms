### [629. K Inverse Pairs Array](https://leetcode.com/problems/k-inverse-pairs-array/)

Hard

For an integer array `` nums ``, an __inverse pair__ is a pair of integers `` [i, j] `` where `` 0 <= i < j < nums.length `` and `` nums[i] > nums[j] ``.

Given two integers n and k, return the number of different arrays consist of numbers from `` 1 `` to `` n `` such that there are exactly `` k `` __inverse pairs__. Since the answer can be huge, return it __modulo__ <code>10<sup>9</sup> + 7</code>.

 

__Example 1:__

```
Input: n = 3, k = 0
Output: 1
Explanation: Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0 inverse pairs.
```

__Example 2:__

```
Input: n = 3, k = 1
Output: 2
Explanation: The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.
```

 

__Constraints:__

*   `` 1 <= n <= 1000 ``
*   `` 0 <= k <= 1000 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 127,998 | 55,263 | 43.2% |