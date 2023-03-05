### [2362. Minimum Rounds to Complete All Tasks](https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/)

Medium

You are given a __0-indexed__ integer array `` tasks ``, where `` tasks[i] `` represents the difficulty level of a task. In each round, you can complete either 2 or 3 tasks of the __same difficulty level__.

Return _the __minimum__ rounds required to complete all the tasks, or _`` -1 ``_ if it is not possible to complete all the tasks._

 

<strong class="example">Example 1:</strong>

```
Input: tasks = [2,2,3,3,2,4,4,4,4,4]
Output: 4
Explanation: To complete all the tasks, a possible plan is:
- In the first round, you complete 3 tasks of difficulty level 2. 
- In the second round, you complete 2 tasks of difficulty level 3. 
- In the third round, you complete 3 tasks of difficulty level 4. 
- In the fourth round, you complete 2 tasks of difficulty level 4.  
It can be shown that all the tasks cannot be completed in fewer than 4 rounds, so the answer is 4.
```

<strong class="example">Example 2:</strong>

```
Input: tasks = [2,3,3]
Output: -1
Explanation: There is only 1 task of difficulty level 2, but in each round, you can only complete either 2 or 3 tasks of the same difficulty level. Hence, you cannot complete all the tasks, and the answer is -1.
```

 

__Constraints:__

*   <code>1 <= tasks.length <= 10<sup>5</sup></code>
*   <code>1 <= tasks[i] <= 10<sup>9</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 205,596 | 129,391 | 62.9% |