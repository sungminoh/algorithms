### [35. Search Insert Position](https://leetcode.com/problems/search-insert-position/)

Easy

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with `` O(log n) `` runtime complexity.

 

__Example 1:__

```Input: nums = [1,3,5,6], target = 5
Output: 2
```

__Example 2:__

```Input: nums = [1,3,5,6], target = 2
Output: 1
```

__Example 3:__

```Input: nums = [1,3,5,6], target = 7
Output: 4
```

__Example 4:__

```Input: nums = [1,3,5,6], target = 0
Output: 0
```

__Example 5:__

```Input: nums = [1], target = 0
Output: 0
```

 

__Constraints:__

*   <code>1 <= nums.length <= 10<sup>4</sup></code>
*   <code>-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup></code>
*   `` nums `` contains __distinct__ values sorted in __ascending__ order.
*   <code>-10<sup>4</sup> <= target <= 10<sup>4</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 2,603,887 | 1,112,272 | 42.7% |