### [35. Search Insert Position](https://leetcode.com/problems/search-insert-position/)

Easy

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with `` O(log n) `` runtime complexity.

 

<strong class="example">Example 1:</strong>

```
Input: nums = [1,3,5,6], target = 5
Output: 2
```

<strong class="example">Example 2:</strong>

```
Input: nums = [1,3,5,6], target = 2
Output: 1
```

<strong class="example">Example 3:</strong>

```
Input: nums = [1,3,5,6], target = 7
Output: 4
```

 

__Constraints:__

*   <code>1 <= nums.length <= 10<sup>4</sup></code>
*   <code>-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup></code>
*   `` nums `` contains __distinct__ values sorted in __ascending__ order.
*   <code>-10<sup>4</sup> <= target <= 10<sup>4</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 4,857,900 | 2,104,672 | 43.3% |