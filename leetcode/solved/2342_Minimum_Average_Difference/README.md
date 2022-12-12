### [2342. Minimum Average Difference](https://leetcode.com/problems/minimum-average-difference/)

Medium

You are given a __0-indexed__ integer array `` nums `` of length `` n ``.

The __average difference__ of the index `` i `` is the __absolute__ __difference__ between the average of the __first__ `` i + 1 `` elements of `` nums `` and the average of the __last__ `` n - i - 1 `` elements. Both averages should be __rounded down__ to the nearest integer.

Return_ the index with the __minimum average difference___. If there are multiple such indices, return the __smallest__ one.

__Note:__

*   The __absolute difference__ of two numbers is the absolute value of their difference.
*   The __average__ of `` n `` elements is the __sum__ of the `` n `` elements divided (__integer division__) by `` n ``.
*   The average of `` 0 `` elements is considered to be `` 0 ``.

 

<strong class="example">Example 1:</strong>

```
Input: nums = [2,5,3,9,5,3]
Output: 3
Explanation:
- The average difference of index 0 is: |2 / 1 - (5 + 3 + 9 + 5 + 3) / 5| = |2 / 1 - 25 / 5| = |2 - 5| = 3.
- The average difference of index 1 is: |(2 + 5) / 2 - (3 + 9 + 5 + 3) / 4| = |7 / 2 - 20 / 4| = |3 - 5| = 2.
- The average difference of index 2 is: |(2 + 5 + 3) / 3 - (9 + 5 + 3) / 3| = |10 / 3 - 17 / 3| = |3 - 5| = 2.
- The average difference of index 3 is: |(2 + 5 + 3 + 9) / 4 - (5 + 3) / 2| = |19 / 4 - 8 / 2| = |4 - 4| = 0.
- The average difference of index 4 is: |(2 + 5 + 3 + 9 + 5) / 5 - 3 / 1| = |24 / 5 - 3 / 1| = |4 - 3| = 1.
- The average difference of index 5 is: |(2 + 5 + 3 + 9 + 5 + 3) / 6 - 0| = |27 / 6 - 0| = |4 - 0| = 4.
The average difference of index 3 is the minimum average difference so return 3.
```

<strong class="example">Example 2:</strong>

```
Input: nums = [0]
Output: 0
Explanation:
The only index is 0 so return 0.
The average difference of index 0 is: |0 / 1 - 0| = |0 - 0| = 0.
```

 

__Constraints:__

*   <code>1 <= nums.length <= 10<sup>5</sup></code>
*   <code>0 <= nums[i] <= 10<sup>5</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 171,956 | 74,178 | 43.1% |