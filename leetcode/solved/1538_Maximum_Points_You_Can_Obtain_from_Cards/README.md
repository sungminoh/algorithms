### [1538. Maximum Points You Can Obtain from Cards](https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/)

Medium

There are several cards __arranged in a row__, and each card has an associated number of points. The points are given in the integer array `` cardPoints ``.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly `` k `` cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array `` cardPoints `` and the integer `` k ``, return the _maximum score_ you can obtain.

 

__Example 1:__

```
Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.
```

__Example 2:__

```
Input: cardPoints = [2,2,2], k = 2
Output: 4
Explanation: Regardless of which two cards you take, your score will always be 4.
```

__Example 3:__

```
Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
Explanation: You have to take all the cards. Your score is the sum of points of all cards.
```

__Example 4:__

```
Input: cardPoints = [1,1000,1], k = 1
Output: 1
Explanation: You cannot take the card in the middle. Your best score is 1. 
```

__Example 5:__

```
Input: cardPoints = [1,79,80,1,1,1,200,1], k = 3
Output: 202
```

 

__Constraints:__

*   <code>1 <= cardPoints.length <= 10<sup>5</sup></code>
*   <code>1 <= cardPoints[i] <= 10<sup>4</sup></code>
*   `` 1 <= k <= cardPoints.length ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 162,751 | 78,648 | 48.3% |