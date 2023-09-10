### [1950. Sign of the Product of an Array](https://leetcode.com/problems/sign-of-the-product-of-an-array/?envType=daily-question&envId=2023-05-02)

Easy

There is a function `` signFunc(x) `` that returns:

*   `` 1 `` if `` x `` is positive.
*   `` -1 `` if `` x `` is negative.
*   `` 0 `` if `` x `` is equal to `` 0 ``.

You are given an integer array `` nums ``. Let `` product `` be the product of all values in the array `` nums ``.

Return `` signFunc(product) ``.

 

<strong class="example">Example 1:</strong>

```
Input: nums = [-1,-2,-3,-4,3,2,1]
Output: 1
Explanation: The product of all values in the array is 144, and signFunc(144) = 1
```

<strong class="example">Example 2:</strong>

```
Input: nums = [1,5,0,2,-3]
Output: 0
Explanation: The product of all values in the array is 0, and signFunc(0) = 0
```

<strong class="example">Example 3:</strong>

```
Input: nums = [-1,1,-1,1,-1]
Output: -1
Explanation: The product of all values in the array is -1, and signFunc(-1) = -1
```

 

__Constraints:__

*   `` 1 <= nums.length <= 1000 ``
*   `` -100 <= nums[i] <= 100 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 449,785 | 294,273 | 65.4% |