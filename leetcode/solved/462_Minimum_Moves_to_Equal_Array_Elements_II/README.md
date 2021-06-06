### [462. Minimum Moves to Equal Array Elements II](https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/)

Medium

Given an integer array `` nums `` of size `` n ``, return _the minimum number of moves required to make all array elements equal_.

In one move, you can increment or decrement an element of the array by `` 1 ``.

Test cases are designed so that the answer will fit in a __32-bit__ integer.

 

__Example 1:__

```
Input: nums = [1,2,3]
Output: 2
Explanation:
Only two moves are needed (remember each move increments or decrements one element):
[<u>1</u>,2,3]  =>  [2,2,<u>3</u>]  =>  [2,2,2]
```

__Example 2:__

```
Input: nums = [1,10,2,9]
Output: 16
```

 

__Constraints:__

*   `` n == nums.length ``
*   <code>1 <= nums.length <= 10<sup>5</sup></code>
*   <code>-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 126,815 | 70,495 | 55.6% |