### [354. Russian Doll Envelopes](https://leetcode.com/problems/russian-doll-envelopes/)

Hard

You are given a 2D array of integers `` envelopes `` where <code>envelopes[i] = [w<sub>i</sub>, h<sub>i</sub>]</code> represents the width and the height of an envelope.

One envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope's width and height.

Return _the maximum number of envelopes you can Russian doll (i.e., put one inside the other)_.

__Note:__ You cannot rotate an envelope.

 

__Example 1:__

<strong>Input:</strong> envelopes = [[5,4],[6,4],[6,7],[2,3]]
    <strong>Output:</strong> 3
    <strong>Explanation:</strong> The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).

__Example 2:__

```
Input: envelopes = [[1,1],[1,1],[1,1]]
Output: 1
```

 

__Constraints:__

*   `` 1 <= envelopes.length <= 5000 ``
*   `` envelopes[i].length == 2 ``
*   <code>1 <= w<sub>i</sub>, h<sub>i</sub> <= 10<sup>4</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 268,960 | 101,507 | 37.7% |