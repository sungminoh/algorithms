### [330. Patching Array](https://leetcode.com/problems/patching-array/)

Hard

Given a sorted positive integer array _nums_ and an integer _n_, add/patch elements to the array such that any number in range `` [1, n] `` inclusive can be formed by the sum of some elements in the array. Return the minimum number of patches required.

__Example 1:__

<strong>Input: </strong><i>nums</i> = [1,3], <i>n</i> = <code>6</code>
<strong>Output: </strong>1 
    <strong>Explanation:</strong>
    Combinations of <i>nums</i> are <code>[1], [3], [1,3]</code>, which form possible sums of: <code>1, 3, 4</code>.
    Now if we add/patch <code>2</code> to <i>nums</i>, the combinations are: <code>[1], [2], [3], [1,3], [2,3], [1,2,3]</code>.
    Possible sums are <code>1, 2, 3, 4, 5, 6</code>, which now covers the range <code>[1, 6]</code>.
    So we only need <code>1</code> patch.

__Example 2:__

<strong>Input: </strong><i>nums</i> = [1,5,10], <i>n</i> = <code>20</code>
<strong>Output:</strong> 2
    <strong>Explanation: </strong>The two patches can be <code>[2, 4]</code>.

__Example 3:__

<strong>Input: </strong><i>nums</i> = [1,2,2], <i>n</i> = <code>5</code>
<strong>Output:</strong> 0

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 107,842 | 37,355 | 34.6% |