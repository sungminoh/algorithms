### [3241. Divide Array Into Arrays With Max Difference](https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/description/?envType=daily-question&envId=2024-02-01)

Medium

You are given an integer array `` nums `` of size `` n `` and a positive integer `` k ``.

Divide the array into one or more arrays of size `` 3 `` satisfying the following conditions:

*   __Each__ element of `` nums `` should be in __exactly__ one array.
*   The difference between __any__ two elements in one array is less than or equal to `` k ``.

Return _a ___2D___ array containing all the arrays. If it is impossible to satisfy the conditions, return an empty array. And if there are multiple answers, return __any__ of them._

 

<strong class="example">Example 1:</strong>

```
Input: nums = [1,3,4,8,7,9,3,5,1], k = 2
Output: [[1,1,3],[3,4,5],[7,8,9]]
Explanation: We can divide the array into the following arrays: [1,1,3], [3,4,5] and [7,8,9].
The difference between any two elements in each array is less than or equal to 2.
Note that the order of elements is not important.
```

<strong class="example">Example 2:</strong>

```
Input: nums = [1,3,3,2,7,3], k = 3
Output: []
Explanation: It is not possible to divide the array satisfying all the conditions.
```

 

__Constraints:__

*   `` n == nums.length ``
*   <code>1 <= n <= 10<sup>5</sup></code>
*   `` n `` is a multiple of `` 3 ``.
*   <code>1 <= nums[i] <= 10<sup>5</sup></code>
*   <code>1 <= k <= 10<sup>5</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 189,885 | 135,766 | 71.5% |