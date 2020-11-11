### [913. Random Flip Matrix](https://leetcode.com/problems/random-flip-matrix/)

Medium

You are given the number of rows `` n_rows `` and number of columns `` n_cols `` of a 2D binary matrix where all values are initially 0. Write a function `` flip `` which chooses a 0 value <a href="https://en.wikipedia.org/wiki/Discrete_uniform_distribution" target="_blank">uniformly at random</a>, changes it to 1, and then returns the position `` [row.id, col.id] `` of that value. Also, write a function `` reset `` which sets all values back to 0. __Try to minimize the number of calls to system's Math.random()__ and optimize the time and space complexity.

Note:

1.   `` 1 <= n_rows, n_cols <= 10000 ``
2.   `` 0 <= row.id < n_rows `` and `` 0 <= col.id < n_cols ``
3.   `` flip `` will not be called when the matrix has no 0 values left.
4.   the total number of calls to `` flip `` and `` reset `` will not exceed 1000.

__Example 1:__

```
Input: 
<span id="example-input-1-1">["Solution","flip","flip","flip","flip"]
</span><span id="example-input-1-2">[[2,3],[],[],[],[]]</span>
Output: <span id="example-output-1">[null,[0,1],[1,2],[1,0],[1,1]]</span>
```

<div>
<p><strong>Example 2:</strong></p>
```
Input: 
<span id="example-input-2-1">["Solution","flip","flip","reset","flip"]
</span><span id="example-input-2-2">[[1,2],[],[],[],[]]</span>
Output: <span id="example-output-2">[null,[0,0],[0,1],null,[0,0]]</span>
```
</div>

__Explanation of Input Syntax:__

The input is two lists: the subroutines called and their arguments. `` Solution ``'s constructor has two arguments, `` n_rows `` and `` n_cols ``. `` flip `` and `` reset `` have no arguments. Arguments are always wrapped with a list, even if there aren't any.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 20,905 | 7,551 | 36.1% |