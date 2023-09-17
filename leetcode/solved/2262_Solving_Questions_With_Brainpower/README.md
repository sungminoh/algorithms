### [2262. Solving Questions With Brainpower](https://leetcode.com/problems/solving-questions-with-brainpower/?envType=daily-question&envId=2023-05-12)

Medium

You are given a __0-indexed__ 2D integer array `` questions `` where <code>questions[i] = [points<sub>i</sub>, brainpower<sub>i</sub>]</code>.

The array describes the questions of an exam, where you have to process the questions __in order__ (i.e., starting from question `` 0 ``) and make a decision whether to __solve__ or __skip__ each question. Solving question `` i `` will __earn__ you <code>points<sub>i</sub></code> points but you will be __unable__ to solve each of the next <code>brainpower<sub>i</sub></code> questions. If you skip question `` i ``, you get to make the decision on the next question.

*   For example, given `` questions = [[3, 2], [4, 3], [4, 4], [2, 5]] ``:	
    
    *   If question `` 0 `` is solved, you will earn `` 3 `` points but you will be unable to solve questions `` 1 `` and `` 2 ``.
    *   If instead, question `` 0 `` is skipped and question `` 1 `` is solved, you will earn `` 4 `` points but you will be unable to solve questions `` 2 `` and `` 3 ``.
    
    
    

Return _the __maximum__ points you can earn for the exam_.

 

<strong class="example">Example 1:</strong>

```
Input: questions = [[3,2],[4,3],[4,4],[2,5]]
Output: 5
Explanation: The maximum points can be earned by solving questions 0 and 3.
- Solve question 0: Earn 3 points, will be unable to solve the next 2 questions
- Unable to solve questions 1 and 2
- Solve question 3: Earn 2 points
Total points earned: 3 + 2 = 5. There is no other way to earn 5 or more points.
```

<strong class="example">Example 2:</strong>

```
Input: questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]
Output: 7
Explanation: The maximum points can be earned by solving questions 1 and 4.
- Skip question 0
- Solve question 1: Earn 2 points, will be unable to solve the next 2 questions
- Unable to solve questions 2 and 3
- Solve question 4: Earn 5 points
Total points earned: 2 + 5 = 7. There is no other way to earn 7 or more points.
```

 

__Constraints:__

*   <code>1 <= questions.length <= 10<sup>5</sup></code>
*   `` questions[i].length == 2 ``
*   <code>1 <= points<sub>i</sub>, brainpower<sub>i</sub> <= 10<sup>5</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 161,539 | 88,906 | 55.0% |