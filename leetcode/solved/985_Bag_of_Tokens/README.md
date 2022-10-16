### [985. Bag of Tokens](https://leetcode.com/problems/bag-of-tokens/)

Medium

You have an initial __power__ of `` power ``, an initial __score__ of `` 0 ``, and a bag of `` tokens `` where `` tokens[i] `` is the value of the <code>i<sup>th</sup></code> token (0-indexed).

Your goal is to maximize your total __score__ by potentially playing each token in one of two ways:

*   If your current __power__ is at least `` tokens[i] ``, you may play the <code>i<sup>th</sup></code> token face up, losing `` tokens[i] `` __power__ and gaining `` 1 `` __score__.
*   If your current __score__ is at least `` 1 ``, you may play the <code>i<sup>th</sup></code> token face down, gaining `` tokens[i] `` __power__ and losing `` 1 `` __score__.

Each token may be played __at most__ once and __in any order__. You do __not__ have to play all the tokens.

Return _the largest possible __score__ you can achieve after playing any number of tokens_.

 

__Example 1:__

```
Input: tokens = [100], power = 50
Output: 0
Explanation: Playing the only token in the bag is impossible because you either have too little power or too little score.
```

__Example 2:__

```
Input: tokens = [100,200], power = 150
Output: 1
Explanation: Play the 0<sup>th</sup> token (100) face up, your power becomes 50 and score becomes 1.
There is no need to play the 1<sup>st</sup> token since you cannot play it face up to add to your score.
```

__Example 3:__

```
Input: tokens = [100,200,300,400], power = 200
Output: 2
Explanation: Play the tokens in this order to get a score of 2:
1. Play the 0<sup>th</sup> token (100) face up, your power becomes 100 and score becomes 1.
2. Play the 3<sup>rd</sup> token (400) face down, your power becomes 500 and score becomes 0.
3. Play the 1<sup>st</sup> token (200) face up, your power becomes 300 and score becomes 1.
4. Play the 2<sup>nd </sup>token (300) face up, your power becomes 0 and score becomes 2.
```

 

__Constraints:__

*   `` 0 <= tokens.length <= 1000 ``
*   <code>0 <= tokens[i], power < 10<sup>4</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 182,842 | 95,187 | 52.1% |