### [1574. Maximum Product of Two Elements in an Array](https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/description/?envType=daily-question&envId=2023-12-12)

Easy

Given the array of integers `` nums ``, you will choose two different indices `` i `` and `` j `` of that array. _Return the maximum value of_ `` (nums[i]-1)*(nums[j]-1) ``.
 

<strong class="example">Example 1:</strong>

```
Input: nums = [3,4,5,2]
Output: 12 
Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12. 
```

<strong class="example">Example 2:</strong>

```
Input: nums = [1,5,4,5]
Output: 16
Explanation: Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum value of (5-1)*(5-1) = 16.
```

<strong class="example">Example 3:</strong>

```
Input: nums = [3,7]
Output: 12
```

 

__Constraints:__

*   `` 2 <= nums.length <= 500 ``
*   `` 1 <= nums[i] <= 10^3 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 421,862 | 347,451 | 82.4% |