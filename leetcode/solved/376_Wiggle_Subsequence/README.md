### [376. Wiggle Subsequence](https://leetcode.com/problems/wiggle-subsequence/)

Medium

A sequence of numbers is called a __wiggle sequence__ if the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.

For example, `` [1,7,4,9,2,5] `` is a wiggle sequence because the differences `` (6,-3,5,-7,3) `` are alternately positive and negative. In contrast, `` [1,4,7,2,5] `` and `` [1,7,4,5,5] `` are not wiggle sequences, the first because its first two differences are positive and the second because its last difference is zero.

Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence. A subsequence is obtained by deleting some number of elements (eventually, also zero) from the original sequence, leaving the remaining elements in their original order.

__Example 1:__

```
<strong>Input: </strong><span id="example-input-1-1">[1,7,4,9,2,5]</span>
<strong>Output: </strong><span id="example-output-1">6
<strong>Explanation:</strong> </span>The entire sequence is a wiggle sequence.```

<div>
<p><strong>Example 2:</strong></p>
```
<strong>Input: </strong><span id="example-input-2-1">[1,17,5,10,13,15,10,5,16,8]</span>
<strong>Output: </strong><span id="example-output-2">7
</span><span id="example-output-1"><strong>Explanation: </strong></span>There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].```
<div>
<p><strong>Example 3:</strong></p>
```
<strong>Input: </strong><span id="example-input-3-1">[1,2,3,4,5,6,7,8,9]</span>
<strong>Output: </strong><span id="example-output-3">2</span>```
<p><b>Follow up:</b><br/>
Can you do it in O(<i>n</i>) time?</p>
</div>
</div>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 158,400 | 61,873 | 39.1% |