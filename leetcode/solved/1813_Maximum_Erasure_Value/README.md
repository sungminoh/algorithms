### [1813. Maximum Erasure Value](https://leetcode.com/problems/maximum-erasure-value/)

Medium

You are given an array of positive integers `` nums `` and want to erase a subarray containing __unique elements__. The __score__ you get by erasing the subarray is equal to the __sum__ of its elements.

Return _the __maximum score__ you can get by erasing __exactly one__ subarray._

An array `` b `` is called to be a <span class="tex-font-style-it">subarray</span> of `` a `` if it forms a contiguous subsequence of `` a ``, that is, if it is equal to `` a[l],a[l+1],...,a[r] `` for some `` (l,r) ``.

 

__Example 1:__

```
Input: nums = [4,2,4,5,6]
Output: 17
Explanation: The optimal subarray here is [2,4,5,6].
```

__Example 2:__

```
Input: nums = [5,2,1,2,5,2,1,2,5]
Output: 8
Explanation: The optimal subarray here is [5,2,1] or [1,2,5].
```

 

__Constraints:__

*   <code>1 <= nums.length <= 10<sup>5</sup></code>
*   <code>1 <= nums[i] <= 10<sup>4</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 166,632 | 96,337 | 57.8% |