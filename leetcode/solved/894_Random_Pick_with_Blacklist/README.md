### [894. Random Pick with Blacklist](https://leetcode.com/problems/random-pick-with-blacklist/)

Hard

Given a blacklist `` B `` containing unique integers from `` [0, N) ``, write a function to return a uniform random integer from `` [0, N) `` which is __NOT__ in `` B ``.

Optimize it such that it minimizes the call to system’s `` Math.random() ``.

__Note:__

1.   `` 1 <= N <= 1000000000 ``
2.   `` 0 <= B.length < min(100000, N) ``
3.   `` [0, N) `` does NOT include N. See <a href="https://en.wikipedia.org/wiki/Interval_(mathematics)" target="_blank">interval notation</a>.

__Example 1:__

```
Input: 
<span id="example-input-1-1">["Solution","pick","pick","pick"]
</span><span id="example-input-1-2">[[1,[]],[],[],[]]</span>
Output: <span id="example-output-1">[null,0,0,0]</span>
```

__Example 2:__

```
Input: 
<span id="example-input-2-1">["Solution","pick","pick","pick"]
</span><span id="example-input-2-2">[[2,[]],[],[],[]]</span>
Output: <span id="example-output-2">[null,1,1,1]</span>
```

__Example 3:__

```
Input: 
<span id="example-input-3-1">["Solution","pick","pick","pick"]
</span><span id="example-input-3-2">[[3,[1]],[],[],[]]</span>
Output: <span id="example-output-3">[null,0,0,2]</span>
```

__Example 4:__

```
Input: 
<span id="example-input-4-1">["Solution","pick","pick","pick"]
</span><span id="example-input-4-2">[[4,[2]],[],[],[]]</span>
Output: <span id="example-output-4">[null,1,3,1]</span>
```

__Explanation of Input Syntax:__

The input is two lists: the subroutines called and their arguments. `` Solution ``'s constructor has two arguments, `` N `` and the blacklist `` B ``. `` pick `` has no arguments. Arguments are always wrapped with a list, even if there aren't any.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 52,359 | 17,175 | 32.8% |