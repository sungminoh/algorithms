### [982. Minimum Increment to Make Array Unique](https://leetcode.com/problems/minimum-increment-to-make-array-unique/)

Medium

Given an array of integers A, a _move_ consists of choosing any `` A[i] ``, and incrementing it by `` 1 ``.

Return the least number of moves to make every value in `` A `` unique.

 

__Example 1:__

```
Input: <span id="example-input-1-1">[1,2,2]</span>
Output: <span id="example-output-1">1</span>
Explanation:  After 1 move, the array could be [1, 2, 3].
```

<div>
<p><strong>Example 2:</strong></p>
```
Input: <span id="example-input-2-1">[3,2,1,2,1,7]</span>
Output: <span id="example-output-2">6</span>
Explanation:  After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.
```
<p> </p>
</div>

__Note:__

1.   `` 0 <= A.length <= 40000 ``
2.   `` 0 <= A[i] < 40000 ``

<div>
<div> </div>
</div>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 51,763 | 23,759 | 45.9% |