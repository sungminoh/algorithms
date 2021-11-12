### [260. Single Number III](https://leetcode.com/problems/single-number-iii/)

Medium

Given an integer array `` nums ``, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in __any order__.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

 

__Example 1:__

```
Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.
```

__Example 2:__

```
Input: nums = [-1,0]
Output: [-1,0]
```

__Example 3:__

```
Input: nums = [0,1]
Output: [1,0]
```

 

__Constraints:__

*   <code>2 <= nums.length <= 3 * 10<sup>4</sup></code>
*   <code>-2<sup>31</sup> <= nums[i] <= 2<sup>31</sup> - 1</code>
*   Each integer in `` nums `` will appear twice, only two integers will appear once.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 347,658 | 232,172 | 66.8% |