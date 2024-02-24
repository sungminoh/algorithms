### [1956. Maximum Element After Decreasing and Rearranging](https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/description/?envType=daily-question&envId=2023-11-15)

Medium

You are given an array of positive integers `` arr ``. Perform some operations (possibly none) on `` arr `` so that it satisfies these conditions:

*   The value of the __first__ element in `` arr `` must be `` 1 ``.
*   The absolute difference between any 2 adjacent elements must be __less than or equal to __`` 1 ``. In other words, `` abs(arr[i] - arr[i - 1]) <= 1 `` for each `` i `` where `` 1 <= i < arr.length `` (__0-indexed__). `` abs(x) `` is the absolute value of `` x ``.

There are 2 types of operations that you can perform any number of times:

*   __Decrease__ the value of any element of `` arr `` to a __smaller positive integer__.
*   __Rearrange__ the elements of `` arr `` to be in any order.

Return _the __maximum__ possible value of an element in _`` arr ``_ after performing the operations to satisfy the conditions_.

 

<strong class="example">Example 1:</strong>

<strong>Input:</strong> arr = [2,2,1,2,1]
    <strong>Output:</strong> 2
    <strong>Explanation:</strong> 
    We can satisfy the conditions by rearranging arr so it becomes <code>[1,2,2,2,1]</code>.
    The largest element in <code>arr</code> is 2.

<strong class="example">Example 2:</strong>

<strong>Input:</strong> arr = [100,1,1000]
    <strong>Output:</strong> 3
    <strong>Explanation:</strong> 
    One possible way to satisfy the conditions is by doing the following:
    1. Rearrange arr so it becomes <code>[1,100,1000]</code>.
    2. Decrease the value of the second element to 2.
    3. Decrease the value of the third element to 3.
    Now <code>arr = [1,2,3]</code>, which<code> </code>satisfies the conditions.
    The largest element in <code>arr is 3.</code>

<strong class="example">Example 3:</strong>

```
Input: arr = [1,2,3,4,5]
Output: 5
Explanation: The array already satisfies the conditions, and the largest element is 5.
```

 

__Constraints:__

*   <code>1 <= arr.length <= 10<sup>5</sup></code>
*   <code>1 <= arr[i] <= 10<sup>9</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 148,823 | 98,212 | 66.0% |