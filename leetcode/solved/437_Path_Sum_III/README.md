### [437. Path Sum III](https://leetcode.com/problems/path-sum-iii/)

Medium

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards(traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

__Example:__

```
root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    <b>5</b>   <b>-3</b>
   <b>/</b> <b>\</b>    <b>\</b>
  <b>3</b>   <b>2</b>   <b>11</b>
 / \   <b>\</b>
3  -2   <b>1</b>

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
```

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 405,179 | 186,644 | 46.1% |