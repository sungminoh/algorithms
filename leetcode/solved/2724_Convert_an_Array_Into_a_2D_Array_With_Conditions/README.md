### [2724. Convert an Array Into a 2D Array With Conditions](https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/description/?envType=daily-question&envId=2024-01-02)

Medium

You are given an integer array `` nums ``. You need to create a 2D array from `` nums `` satisfying the following conditions:

*   The 2D array should contain __only__ the elements of the array `` nums ``.
*   Each row in the 2D array contains __distinct__ integers.
*   The number of rows in the 2D array should be __minimal__.

Return _the resulting array_. If there are multiple answers, return any of them.

__Note__ that the 2D array can have a different number of elements on each row.

 

<strong class="example">Example 1:</strong>

```
Input: nums = [1,3,4,1,2,3,1]
Output: [[1,3,4,2],[1,3],[1]]
Explanation: We can create a 2D array that contains the following rows:
- 1,3,4,2
- 1,3
- 1
All elements of nums were used, and each row of the 2D array contains distinct integers, so it is a valid answer.
It can be shown that we cannot have less than 3 rows in a valid array.
```

<strong class="example">Example 2:</strong>

```
Input: nums = [1,2,3,4]
Output: [[4,3,2,1]]
Explanation: All elements of the array are distinct, so we can keep all of them in the first row of the 2D array.
```

 

__Constraints:__

*   `` 1 <= nums.length <= 200 ``
*   `` 1 <= nums[i] <= nums.length ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 203,793 | 178,338 | 87.5% |