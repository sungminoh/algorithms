### [508. Most Frequent Subtree Sum](https://leetcode.com/problems/most-frequent-subtree-sum/)

Medium

Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.

__Examples 1__  
Input:

```
  5
 /  \
2   -3
```

return \[2, -3, 4\], since all the values happen only once, return all of them in any order.

__Examples 2__  
Input:

```
  5
 /  \
2   -5
```

return \[2\], since 2 happens twice, however -5 only occur once.

__Note:__You may assume the sum of values in any subtree is in the range of 32-bit signed integer.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 117,572 | 67,348 | 57.3% |