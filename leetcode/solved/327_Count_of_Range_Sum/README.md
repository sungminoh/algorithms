### [327. Count of Range Sum](https://leetcode.com/problems/count-of-range-sum/)

Hard

Given an integer array `` nums ``, return the number of range sums that lie in `` [lower, upper] `` inclusive.  
Range sum `` S(i, j) `` is defined as the sum of the elements in `` nums `` between indices `` i `` and `` j `` (`` i `` ≤ `` j ``), inclusive.

__Note:__  
A naive algorithm of _O_(_n_<sup>2</sup>) is trivial. You MUST do better than that.

__Example:__

<strong>Input: </strong><i>nums</i> = [-2,5,-1], <i>lower</i> = <code>-2</code>, <i>upper</i> = <code>2</code>,
    <strong>Output: </strong>3 
    <strong>Explanation: </strong>The three ranges are : <code>[0,0]</code>, <code>[2,2]</code>, <code>[0,2]</code> and their respective sums are: <code>-2, -1, 2</code>.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 119,468 | 41,586 | 34.8% |