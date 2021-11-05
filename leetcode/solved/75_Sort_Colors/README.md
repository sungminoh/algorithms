### [75. Sort Colors](https://leetcode.com/problems/sort-colors/)

Medium

Given an array `` nums `` with `` n `` objects colored red, white, or blue, sort them __<a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in-place</a> __so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers `` 0 ``, `` 1 ``, and `` 2 `` to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

__Example 1:__

```Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
```

__Example 2:__

```Input: nums = [2,0,1]
Output: [0,1,2]
```

__Example 3:__

```Input: nums = [0]
Output: [0]
```

__Example 4:__

```Input: nums = [1]
Output: [1]
```

 

__Constraints:__

*   `` n == nums.length ``
*   `` 1 <= n <= 300 ``
*   `` nums[i] `` is `` 0 ``, `` 1 ``, or `` 2 ``.

 

__Follow up:__ Could you come up with a one-pass algorithm using only constant extra space?

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 1,580,110 | 834,318 | 52.8% |