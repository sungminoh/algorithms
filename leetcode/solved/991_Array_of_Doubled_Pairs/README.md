### [991. Array of Doubled Pairs](https://leetcode.com/problems/array-of-doubled-pairs/)

Medium

Given an integer array of even length `` arr ``, return `` true ``_ if it is possible to reorder _`` arr ``_ such that _`` arr[2 * i + 1] = 2 * arr[2 * i] ``_ for every _`` 0 <= i < len(arr) / 2 ``_, or _`` false ``_ otherwise_.

 

__Example 1:__

```
Input: arr = [3,1,3,6]
Output: false
```

__Example 2:__

```
Input: arr = [2,1,2,6]
Output: false
```

__Example 3:__

```
Input: arr = [4,-2,2,-4]
Output: true
Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].
```

__Example 4:__

```
Input: arr = [1,2,4,16,8,4]
Output: false
```

 

__Constraints:__

*   <code>2 <= arr.length <= 3 * 10<sup>4</sup></code>
*   `` arr.length `` is even.
*   <code>-10<sup>5</sup> <= arr[i] <= 10<sup>5</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 141,910 | 51,776 | 36.5% |