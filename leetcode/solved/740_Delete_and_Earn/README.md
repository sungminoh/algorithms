### [740. Delete and Earn](https://leetcode.com/problems/delete-and-earn/)

Medium

Given an array `` nums `` of integers, you can perform operations on the array.

In each operation, you pick any `` nums[i] `` and delete it to earn `` nums[i] `` points. After, you must delete __every__ element equal to `` nums[i] - 1 `` or `` nums[i] + 1 ``.

You start with 0 points. Return the maximum number of points you can earn by applying such operations.

__Example 1:__

```
<b>Input:</b> nums = [3, 4, 2]
<b>Output:</b> 6
<b>Explanation:</b> 
Delete 4 to earn 4 points, consequently 3 is also deleted.
Then, delete 2 to earn 2 points. 6 total points are earned.
```

 

__Example 2:__

```
<b>Input:</b> nums = [2, 2, 3, 3, 3, 4]
<b>Output:</b> 9
<b>Explanation:</b> 
Delete 3 to earn 3 points, deleting both 2's and the 4.
Then, delete 3 again to earn 3 points, and 3 again to earn 3 points.
9 total points are earned.
```

 

__Note:__

*   The length of `` nums `` is at most `` 20000 ``.
*   Each element `` nums[i] `` is an integer in the range `` [1, 10000] ``.

 

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 82,962 | 40,441 | 48.7% |