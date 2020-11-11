### [503. Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/)

Medium

Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

__Example 1:__  

```
<b>Input:</b> [1,2,1]
<b>Output:</b> [2,-1,2]
<b>Explanation:</b> The first 1's next greater number is 2; 
```

The number 2 can't find next greater number; The second 1's next greater number needs to search circularly, which is also 2.

__Note:__The length of given array won't exceed 10000.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 157,970 | 87,470 | 55.4% |