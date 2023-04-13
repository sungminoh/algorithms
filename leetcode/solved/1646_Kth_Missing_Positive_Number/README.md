### [1646. Kth Missing Positive Number](https://leetcode.com/problems/kth-missing-positive-number/)

Easy

Given an array `` arr `` of positive integers sorted in a __strictly increasing order__, and an integer `` k ``.

Return _the_ <code>k<sup>th</sup></code> ___positive__ integer that is __missing__ from this array._

 

<strong class="example">Example 1:</strong>

```
Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5<sup>th</sup> missing positive integer is 9.
```

<strong class="example">Example 2:</strong>

```
Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2<sup>nd</sup> missing positive integer is 6.
```

 

__Constraints:__

*   `` 1 <= arr.length <= 1000 ``
*   `` 1 <= arr[i] <= 1000 ``
*   `` 1 <= k <= 1000 ``
*   `` arr[i] < arr[j] `` for `` 1 <= i < j <= arr.length ``

 

__Follow up:__

Could you solve this problem in less than O(n) complexity?

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 511,930 | 299,913 | 58.6% |