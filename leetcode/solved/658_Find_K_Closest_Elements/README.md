### [658. Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements/)

Medium

Given a __sorted__ integer array `` arr ``, two integers `` k `` and `` x ``, return the `` k `` closest integers to `` x `` in the array. The result should also be sorted in ascending order.

An integer `` a `` is closer to `` x `` than an integer `` b `` if:

*   `` |a - x| < |b - x| ``, or
*   `` |a - x| == |b - x| `` and `` a < b ``

 

<strong class="example">Example 1:</strong>

```Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
```

<strong class="example">Example 2:</strong>

```Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]
```

 

__Constraints:__

*   `` 1 <= k <= arr.length ``
*   <code>1 <= arr.length <= 10<sup>4</sup></code>
*   `` arr `` is sorted in __ascending__ order.
*   <code>-10<sup>4</sup> <= arr[i], x <= 10<sup>4</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 835,407 | 390,344 | 46.7% |