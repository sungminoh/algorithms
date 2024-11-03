### [1556. Make Two Arrays Equal by Reversing Subarrays](https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/description/?envType=daily-question&envId=2024-08-03)

Easy

You are given two integer arrays of equal length `` target `` and `` arr ``. In one step, you can select any __non-empty subarray__ of `` arr `` and reverse it. You are allowed to make any number of steps.

Return `` true `` _if you can make _`` arr ``_ equal to _`` target ``_ or _`` false ``_ otherwise_.

 

<strong class="example">Example 1:</strong>

```
Input: target = [1,2,3,4], arr = [2,4,1,3]
Output: true
Explanation: You can follow the next steps to convert arr to target:
1- Reverse subarray [2,4,1], arr becomes [1,4,2,3]
2- Reverse subarray [4,2], arr becomes [1,2,4,3]
3- Reverse subarray [4,3], arr becomes [1,2,3,4]
There are multiple ways to convert arr to target, this is not the only way to do so.
```

<strong class="example">Example 2:</strong>

```
Input: target = [7], arr = [7]
Output: true
Explanation: arr is equal to target without any reverses.
```

<strong class="example">Example 3:</strong>

```
Input: target = [3,7,9], arr = [3,7,11]
Output: false
Explanation: arr does not have value 9 and it can never be converted to target.
```

 

__Constraints:__

*   `` target.length == arr.length ``
*   `` 1 <= target.length <= 1000 ``
*   `` 1 <= target[i] <= 1000 ``
*   `` 1 <= arr[i] <= 1000 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 400,454 | 304,220 | 76.0% |