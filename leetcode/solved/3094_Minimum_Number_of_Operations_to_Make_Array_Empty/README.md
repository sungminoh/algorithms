### [3094. Minimum Number of Operations to Make Array Empty](https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/description/?envType=daily-question&envId=2024-01-04)

Medium

You are given a __0-indexed__ array `` nums `` consisting of positive integers.

There are two types of operations that you can apply on the array __any__ number of times:

*   Choose __two__ elements with __equal__ values and __delete__ them from the array.
*   Choose __three__ elements with __equal__ values and __delete__ them from the array.

Return _the __minimum__ number of operations required to make the array empty, or _`` -1 ``_ if it is not possible_.

 

<strong class="example">Example 1:</strong>

```
Input: nums = [2,3,3,2,2,4,2,3,4]
Output: 4
Explanation: We can apply the following operations to make the array empty:
- Apply the first operation on the elements at indices 0 and 3. The resulting array is nums = [3,3,2,4,2,3,4].
- Apply the first operation on the elements at indices 2 and 4. The resulting array is nums = [3,3,4,3,4].
- Apply the second operation on the elements at indices 0, 1, and 3. The resulting array is nums = [4,4].
- Apply the first operation on the elements at indices 0 and 1. The resulting array is nums = [].
It can be shown that we cannot make the array empty in less than 4 operations.
```

<strong class="example">Example 2:</strong>

```
Input: nums = [2,1,2,2,3,3]
Output: -1
Explanation: It is impossible to empty the array.
```

 

__Constraints:__

*   <code>2 <= nums.length <= 10<sup>5</sup></code>
*   <code>1 <= nums[i] <= 10<sup>6</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 256,507 | 158,504 | 61.8% |