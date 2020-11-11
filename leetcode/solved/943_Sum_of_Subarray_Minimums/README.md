### [943. Sum of Subarray Minimums](https://leetcode.com/problems/sum-of-subarray-minimums/)

Medium

Given an array of integers `` A ``, find the sum of `` min(B) ``, where `` B `` ranges over every (contiguous) subarray of `` A ``.

Since the answer may be large, __return the answer modulo `` 10^9 + 7 ``.__

 

__Example 1:__

```
Input: <span id="example-input-1-1">[3,1,2,4]</span>
Output: <span id="example-output-1">17</span>
Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.
```

 

__Note:__

1.   `` 1 <= A.length <= 30000 ``
2.   `` 1 <= A[i] <= 30000 ``

<div>
<p> </p>
</div>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 71,760 | 22,517 | 31.4% |