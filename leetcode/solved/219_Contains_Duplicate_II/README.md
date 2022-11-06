### [219. Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/)

Easy

Given an integer array `` nums `` and an integer `` k ``, return `` true `` _if there are two __distinct indices__ _`` i ``_ and _`` j ``_ in the array such that _`` nums[i] == nums[j] ``_ and _`` abs(i - j) <= k ``.

 

<strong class="example">Example 1:</strong>

```
Input: nums = [1,2,3,1], k = 3
Output: true
```

<strong class="example">Example 2:</strong>

```
Input: nums = [1,0,1,1], k = 1
Output: true
```

<strong class="example">Example 3:</strong>

```
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
```

 

__Constraints:__

*   <code>1 <= nums.length <= 10<sup>5</sup></code>
*   <code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code>
*   <code>0 <= k <= 10<sup>5</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 1,431,803 | 605,328 | 42.3% |