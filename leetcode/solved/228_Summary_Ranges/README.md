### [228. Summary Ranges](https://leetcode.com/problems/summary-ranges/)

Easy

You are given a __sorted unique__ integer array `` nums ``.

Return _the __smallest sorted__ list of ranges that __cover all the numbers in the array exactly___. That is, each element of `` nums `` is covered by exactly one of the ranges, and there is no integer `` x `` such that `` x `` is in one of the ranges but not in `` nums ``.

Each range `` [a,b] `` in the list should be output as:

*   `` "a->b" `` if `` a != b ``
*   `` "a" `` if `` a == b ``

 

__Example 1:__

```
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
```

__Example 2:__

```
Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
```

 

__Constraints:__

*   `` 0 <= nums.length <= 20 ``
*   <code>-2<sup>31</sup> <= nums[i] <= 2<sup>31</sup> - 1</code>
*   All the values of `` nums `` are __unique__.
*   `` nums `` is sorted in ascending order.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 620,765 | 286,981 | 46.2% |