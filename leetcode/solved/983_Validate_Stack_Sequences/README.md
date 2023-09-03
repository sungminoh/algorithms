### [983. Validate Stack Sequences](https://leetcode.com/problems/validate-stack-sequences/?envType=daily-question&envId=2023-04-13)

Medium

Given two integer arrays `` pushed `` and `` popped `` each with distinct values, return `` true ``_ if this could have been the result of a sequence of push and pop operations on an initially empty stack, or _`` false ``_ otherwise._

 

<strong class="example">Example 1:</strong>

```
Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4),
pop() -> 4,
push(5),
pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
```

<strong class="example">Example 2:</strong>

```
Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.
```

 

__Constraints:__

*   `` 1 <= pushed.length <= 1000 ``
*   `` 0 <= pushed[i] <= 1000 ``
*   All the elements of `` pushed `` are __unique__.
*   `` popped.length == pushed.length ``
*   `` popped `` is a permutation of `` pushed ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 405,020 | 281,111 | 69.4% |