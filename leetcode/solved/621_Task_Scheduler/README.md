### [621. Task Scheduler](https://leetcode.com/problems/task-scheduler/)

Medium

Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks. Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval __n__ that means between two __same tasks__, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the __least__ number of intervals the CPU will take to finish all the given tasks.

 

__Example:__

```
<b>Input:</b> tasks = ["A","A","A","B","B","B"], n = 2
<b>Output:</b> 8
<b>Explanation:</b> A -> B -> idle -> A -> B -> idle -> A -> B.
```

 

__Constraints:__

*   The number of tasks is in the range `` [1, 10000] ``.
*   The integer `` n `` is in the range `` [0, 100] ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 334,373 | 161,279 | 48.2% |