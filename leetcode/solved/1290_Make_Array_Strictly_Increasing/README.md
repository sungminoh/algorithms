### [1290. Make Array Strictly Increasing](https://leetcode.com/problems/make-array-strictly-increasing/description/)

Hard

Given two integer arrays `` arr1 `` and `` arr2 ``, return the minimum number of operations (possibly zero) needed to make `` arr1 `` strictly increasing.

In one operation, you can choose two indices `` 0 <= i < arr1.length `` and `` 0 <= j < arr2.length `` and do the assignment `` arr1[i] = arr2[j] ``.

If there is no way to make `` arr1 `` strictly increasing, return `` -1 ``.

 

<strong class="example">Example 1:</strong>

<strong>Input:</strong> arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]
    <strong>Output:</strong> 1
    <strong>Explanation:</strong> Replace 5 with <code>2</code>, then <code>arr1 = [1, 2, 3, 6, 7]</code>.

<strong class="example">Example 2:</strong>

<strong>Input:</strong> arr1 = [1,5,3,6,7], arr2 = [4,3,1]
    <strong>Output:</strong> 2
    <strong>Explanation:</strong> Replace 5 with <code>3</code> and then replace <code>3</code> with <code>4</code>. <code>arr1 = [1, 3, 4, 6, 7]</code>.

<strong class="example">Example 3:</strong>

<strong>Input:</strong> arr1 = [1,5,3,6,7], arr2 = [1,6,3,3]
    <strong>Output:</strong> -1
    <strong>Explanation:</strong> You can't make arr1 strictly increasing.

 

__Constraints:__

*   `` 1 <= arr1.length, arr2.length <= 2000 ``
*   `` 0 <= arr1[i], arr2[i] <= 10^9 ``

 

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 98,173 | 57,254 | 58.3% |