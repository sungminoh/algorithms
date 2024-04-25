### [823. Split Array With Same Average](https://leetcode.com/problems/split-array-with-same-average/description/)

Hard

You are given an integer array `` nums ``.

You should move each element of `` nums `` into one of the two arrays `` A `` and `` B `` such that `` A `` and `` B `` are non-empty, and `` average(A) == average(B) ``.

Return `` true `` if it is possible to achieve that and `` false `` otherwise.

__Note__ that for an array `` arr ``, `` average(arr) `` is the sum of all the elements of `` arr `` over the length of `` arr ``.

 

<strong class="example">Example 1:</strong>

```
Input: nums = [1,2,3,4,5,6,7,8]
Output: true
Explanation: We can split the array into [1,4,5,8] and [2,3,6,7], and both of them have an average of 4.5.
```

<strong class="example">Example 2:</strong>

```
Input: nums = [3,1]
Output: false
```

 

__Constraints:__

*   `` 1 <= nums.length <= 30 ``
*   <code>0 <= nums[i] <= 10<sup>4</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 138,016 | 35,035 | 25.4% |