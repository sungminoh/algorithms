### [1985. Maximum Subarray Min-Product](https://leetcode.com/problems/maximum-subarray-min-product/description/)

Medium

The __min-product__ of an array is equal to the __minimum value__ in the array __multiplied by__ the array's __sum__.

*   For example, the array `` [3,2,5] `` (minimum value is `` 2 ``) has a min-product of `` 2 * (3+2+5) = 2 * 10 = 20 ``.

Given an array of integers `` nums ``, return _the __maximum min-product__ of any __non-empty subarray__ of _`` nums ``. Since the answer may be large, return it __modulo__ <code>10<sup>9</sup> + 7</code>.

Note that the min-product should be maximized __before__ performing the modulo operation. Testcases are generated such that the maximum min-product __without__ modulo will fit in a __64-bit signed integer__.

A __subarray__ is a __contiguous__ part of an array.

 

<strong class="example">Example 1:</strong>

```
Input: nums = [1,<u>2,3,2</u>]
Output: 14
Explanation: The maximum min-product is achieved with the subarray [2,3,2] (minimum value is 2).
2 * (2+3+2) = 2 * 7 = 14.
```

<strong class="example">Example 2:</strong>

```
Input: nums = [2,<u>3,3</u>,1,2]
Output: 18
Explanation: The maximum min-product is achieved with the subarray [3,3] (minimum value is 3).
3 * (3+3) = 3 * 6 = 18.
```

<strong class="example">Example 3:</strong>

```
Input: nums = [3,1,<u>5,6,4</u>,2]
Output: 60
Explanation: The maximum min-product is achieved with the subarray [5,6,4] (minimum value is 4).
4 * (5+6+4) = 4 * 15 = 60.
```

 

__Constraints:__

*   <code>1 <= nums.length <= 10<sup>5</sup></code>
*   <code>1 <= nums[i] <= 10<sup>7</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 80,484 | 30,942 | 38.4% |