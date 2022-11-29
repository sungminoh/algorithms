### [632. Smallest Range Covering Elements from K Lists](https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/)

Hard

You have `` k `` lists of sorted integers in __non-decreasing order__. Find the __smallest__ range that includes at least one number from each of the `` k `` lists.

We define the range `` [a, b] `` is smaller than range `` [c, d] `` if `` b - a < d - c `` __or__ `` a < c `` if `` b - a == d - c ``.

 

<strong class="example">Example 1:</strong>

```
Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20,24]
Explanation: 
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].
```

<strong class="example">Example 2:</strong>

```
Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
Output: [1,1]
```

 

__Constraints:__

*   `` nums.length == k ``
*   `` 1 <= k <= 3500 ``
*   `` 1 <= nums[i].length <= 50 ``
*   <code>-10<sup>5</sup> <= nums[i][j] <= 10<sup>5</sup></code>
*   `` nums[i] `` is sorted in __non-decreasing__ order.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 130,164 | 78,863 | 60.6% |