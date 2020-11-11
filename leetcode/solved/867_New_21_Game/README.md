### [867. New 21 Game](https://leetcode.com/problems/new-21-game/)

Medium

Alice plays the following game, loosely based on the card game "21".

Alice starts with `` 0 `` points, and draws numbers while she has less than `` K `` points.  During each draw, she gains an integer number of points randomly from the range `` [1, W] ``, where `` W `` is an integer.  Each draw is independent and the outcomes have equal probabilities.

Alice stops drawing numbers when she gets `` K `` or more points.  What is the probability that she has `` N `` or less points?

__Example 1:__

```
Input: N = 10, K = 1, W = 10
Output: 1.00000
Explanation:  Alice gets a single card, then stops.
```

__Example 2:__

```
Input: N = 6, K = 1, W = 10
Output: 0.60000
Explanation:  Alice gets a single card, then stops.
In 6 out of W = 10 possibilities, she is at or below N = 6 points.
```

__Example 3:__

```
Input: N = 21, K = 17, W = 10
Output: 0.73278
```

__Note:__

1.   `` 0 <= K <= N <= 10000 ``
2.   `` 1 <= W <= 10000 ``
3.   Answers will be accepted as correct if they are within `` 10^-5 `` of the correct answer.
4.   The judging time limit has been reduced for this question.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 54,373 | 19,030 | 35.0% |