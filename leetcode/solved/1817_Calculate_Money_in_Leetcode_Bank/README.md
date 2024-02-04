### [1817. Calculate Money in Leetcode Bank](https://leetcode.com/problems/calculate-money-in-leetcode-bank/description/?envType=daily-question&envId=2023-12-06)

Easy

Hercy wants to save money for his first car. He puts money in the Leetcode bank __every day__.

He starts by putting in `` $1 `` on Monday, the first day. Every day from Tuesday to Sunday, he will put in `` $1 `` more than the day before. On every subsequent Monday, he will put in `` $1 `` more than the __previous Monday__.<span style="display: none;"> </span>

Given `` n ``, return _the total amount of money he will have in the Leetcode bank at the end of the _<code>n<sup>th</sup></code>_ day._

 

<strong class="example">Example 1:</strong>

```
Input: n = 4
Output: 10
Explanation: After the 4<sup>th</sup> day, the total is 1 + 2 + 3 + 4 = 10.
```

<strong class="example">Example 2:</strong>

```
Input: n = 10
Output: 37
Explanation: After the 10<sup>th</sup> day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37. Notice that on the 2<sup>nd</sup> Monday, Hercy only puts in $2.
```

<strong class="example">Example 3:</strong>

```
Input: n = 20
Output: 96
Explanation: After the 20<sup>th</sup> day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96.
```

 

__Constraints:__

*   `` 1 <= n <= 1000 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 190,136 | 148,610 | 78.2% |