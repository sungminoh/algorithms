### [456. 132 Pattern](https://leetcode.com/problems/132-pattern/)

Medium

Given a sequence of n integers a<sub>1</sub>, a<sub>2</sub>, ..., a<sub>n</sub>, a 132 pattern is a subsequence a<sub>__i__</sub>, a<sub>__j__</sub>, a<sub>__k__</sub> suchthat __i__ < __j__ < __k__ and a<sub>__i__</sub> < a<sub>__k__</sub> < a<sub>__j__</sub>. Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.

__Note:__ n will be less than 15,000.

__Example 1:__  

```
<b>Input:</b> [1, 2, 3, 4]

<b>Output:</b> False

<b>Explanation:</b> There is no 132 pattern in the sequence.
```

__Example 2:__  

```
<b>Input:</b> [3, 1, 4, 2]

<b>Output:</b> True

<b>Explanation:</b> There is a 132 pattern in the sequence: [1, 4, 2].
```

__Example 3:__  

```
<b>Input:</b> [-1, 3, 2, 0]

<b>Output:</b> True

<b>Explanation:</b> There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
```

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 175,429 | 50,676 | 28.9% |