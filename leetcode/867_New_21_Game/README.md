### [867. New 21 Game](https://leetcode.com/problems/new-21-game/description/?envType=daily-question&envId=2025-08-17)

Medium

Alice plays the following game, loosely based on the card game __"21"__.

Alice starts with `` 0 `` points and draws numbers while she has less than `` k `` points. During each draw, she gains an integer number of points randomly from the range `` [1, maxPts] ``, where `` maxPts `` is an integer. Each draw is independent and the outcomes have equal probabilities.

Alice stops drawing numbers when she gets `` k `` __or more points__.

Return the probability that Alice has `` n `` or fewer points.

Answers within <code>10<sup>-5</sup></code> of the actual answer are considered accepted.

 

<strong class="example">Example 1:</strong>

```
Input: n = 10, k = 1, maxPts = 10
Output: 1.00000
Explanation: Alice gets a single card, then stops.
```

<strong class="example">Example 2:</strong>

```
Input: n = 6, k = 1, maxPts = 10
Output: 0.60000
Explanation: Alice gets a single card, then stops.
In 6 out of 10 possibilities, she is at or below 6 points.
```

<strong class="example">Example 3:</strong>

```
Input: n = 21, k = 17, maxPts = 10
Output: 0.73278
```

 

__Constraints:__

*   <code>0 <= k <= n <= 10<sup>4</sup></code>
*   <code>1 <= maxPts <= 10<sup>4</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 297,480 | 154,887 | 52.1% |