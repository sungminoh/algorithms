### [1748. Best Team With No Conflicts](https://leetcode.com/problems/best-team-with-no-conflicts/)

Medium

You are the manager of a basketball team. For the upcoming tournament, you want to choose the team with the highest overall score. The score of the team is the __sum__ of scores of all the players in the team.

However, the basketball team is not allowed to have __conflicts__. A __conflict__ exists if a younger player has a __strictly higher__ score than an older player. A conflict does __not__ occur between players of the same age.

Given two lists, `` scores `` and `` ages ``, where each `` scores[i] `` and `` ages[i] `` represents the score and age of the <code>i<sup>th</sup></code> player, respectively, return _the highest overall score of all possible basketball teams_.

 

<strong class="example">Example 1:</strong>

```
Input: scores = [1,3,5,10,15], ages = [1,2,3,4,5]
Output: 34
Explanation: You can choose all the players.
```

<strong class="example">Example 2:</strong>

```
Input: scores = [4,5,6,5], ages = [2,1,2,1]
Output: 16
Explanation: It is best to choose the last 3 players. Notice that you are allowed to choose multiple people of the same age.
```

<strong class="example">Example 3:</strong>

```
Input: scores = [1,2,3,5], ages = [8,9,10,1]
Output: 6
Explanation: It is best to choose the first 3 players. 
```

 

__Constraints:__

*   `` 1 <= scores.length, ages.length <= 1000 ``
*   `` scores.length == ages.length ``
*   <code>1 <= scores[i] <= 10<sup>6</sup></code>
*   `` 1 <= ages[i] <= 1000 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 137,246 | 70,187 | 51.1% |