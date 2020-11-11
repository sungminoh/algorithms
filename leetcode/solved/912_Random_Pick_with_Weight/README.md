### [912. Random Pick with Weight](https://leetcode.com/problems/random-pick-with-weight/)

Medium

Given an array `` w `` of positive integers, where `` w[i] `` describes the weight of index `` i ``, write a function `` pickIndex `` which randomly picks an index in proportion to its weight.

Note:

1.   `` 1 <= w.length <= 10000 ``
2.   `` 1 <= w[i] <= 10^5 ``
3.   `` pickIndex `` will be called at most `` 10000 `` times.

__Example 1:__

```
Input: 
<span id="example-input-1-1">["Solution","pickIndex"]
</span><span id="example-input-1-2">[[[1]],[]]</span>
Output: <span id="example-output-1">[null,0]</span>
```

<div>
<p><strong>Example 2:</strong></p>
```
Input: 
<span id="example-input-2-1">["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
</span><span id="example-input-2-2">[[[1,3]],[],[],[],[],[]]</span>
Output: <span id="example-output-2">[null,0,1,1,1,0]</span>
```
</div>

__Explanation of Input Syntax:__

The input is two lists: the subroutines called and their arguments. `` Solution ``'s constructor has one argument, the array `` w ``. `` pickIndex `` has no arguments. Arguments are always wrapped with a list, even if there aren't any.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 142,357 | 62,342 | 43.8% |