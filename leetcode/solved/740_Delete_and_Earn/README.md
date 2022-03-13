### [740. Delete and Earn](https://leetcode.com/problems/delete-and-earn/)

Medium

You are given an integer array `` nums ``. You want to maximize the number of points you get by performing the following operation any number of times:

*   Pick any `` nums[i] `` and delete it to earn `` nums[i] `` points. Afterwards, you must delete __every__ element equal to `` nums[i] - 1 `` and __every__ element equal to `` nums[i] + 1 ``.

Return _the __maximum number of points__ you can earn by applying the above operation some number of times_.

 

__Example 1:__

```
Input: nums = [3,4,2]
Output: 6
Explanation: You can perform the following operations:
- Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
- Delete 2 to earn 2 points. nums = [].
You earn a total of 6 points.
```

__Example 2:__

```
Input: nums = [2,2,3,3,3,4]
Output: 9
Explanation: You can perform the following operations:
- Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
- Delete a 3 again to earn 3 points. nums = [3].
- Delete a 3 once more to earn 3 points. nums = [].
You earn a total of 9 points.
```

 

__Constraints:__

*   <code>1 <= nums.length <= 2 * 10<sup>4</sup></code>
*   <code>1 <= nums[i] <= 10<sup>4</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 289,559 | 165,184 | 57.0% |