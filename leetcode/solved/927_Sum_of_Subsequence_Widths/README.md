### [927. Sum of Subsequence Widths](https://leetcode.com/problems/sum-of-subsequence-widths/description/)

Hard

The __width__ of a sequence is the difference between the maximum and minimum elements in the sequence.

Given an array of integers `` nums ``, return _the sum of the __widths__ of all the non-empty __subsequences__ of _`` nums ``. Since the answer may be very large, return it __modulo__ <code>10<sup>9</sup> + 7</code>.

A __subsequence__ is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, `` [3,6,2,7] `` is a subsequence of the array `` [0,3,1,6,2,2,7] ``.

 

<strong class="example">Example 1:</strong>

```
Input: nums = [2,1,3]
Output: 6
Explanation: The subsequences are [1], [2], [3], [2,1], [2,3], [1,3], [2,1,3].
The corresponding widths are 0, 0, 0, 1, 1, 2, 2.
The sum of these widths is 6.
```

<strong class="example">Example 2:</strong>

```
Input: nums = [2]
Output: 0
```

 

__Constraints:__

*   <code>1 <= nums.length <= 10<sup>5</sup></code>
*   <code>1 <= nums[i] <= 10<sup>5</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 55,549 | 20,973 | 37.8% |