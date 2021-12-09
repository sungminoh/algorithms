### [152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)

Medium

Given an integer array `` nums ``, find a contiguous non-empty subarray within the array that has the largest product, and return _the product_.

The test cases are generated so that the answer will fit in a __32-bit__ integer.

A __subarray__ is a contiguous subsequence of the array.

 

__Example 1:__

```
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
```

__Example 2:__

```
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
```

 

__Constraints:__

*   <code>1 <= nums.length <= 2 * 10<sup>4</sup></code>
*   `` -10 <= nums[i] <= 10 ``
*   The product of any prefix or suffix of `` nums `` is __guaranteed__ to fit in a __32-bit__ integer.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 1,817,875 | 619,446 | 34.1% |