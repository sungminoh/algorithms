### [1605. Minimum Number of Days to Make m Bouquets](https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/description/?envType=daily-question&envId=2024-06-19)

Medium

You are given an integer array `` bloomDay ``, an integer `` m `` and an integer `` k ``.

You want to make `` m `` bouquets. To make a bouquet, you need to use `` k `` __adjacent flowers__ from the garden.

The garden consists of `` n `` flowers, the <code>i<sup>th</sup></code> flower will bloom in the `` bloomDay[i] `` and then can be used in __exactly one__ bouquet.

Return _the minimum number of days you need to wait to be able to make _`` m ``_ bouquets from the garden_. If it is impossible to make m bouquets return `` -1 ``.

 

<strong class="example">Example 1:</strong>

```
Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
Output: 3
Explanation: Let us see what happened in the first three days. x means flower bloomed and _ means flower did not bloom in the garden.
We need 3 bouquets each should contain 1 flower.
After day 1: [x, _, _, _, _]   // we can only make one bouquet.
After day 2: [x, _, _, _, x]   // we can only make two bouquets.
After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.
```

<strong class="example">Example 2:</strong>

```
Input: bloomDay = [1,10,3,10,2], m = 3, k = 2
Output: -1
Explanation: We need 3 bouquets each has 2 flowers, that means we need 6 flowers. We only have 5 flowers so it is impossible to get the needed bouquets and we return -1.
```

<strong class="example">Example 3:</strong>

```
Input: bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3
Output: 12
Explanation: We need 2 bouquets each should have 3 flowers.
Here is the garden after the 7 and 12 days:
After day 7: [x, x, x, x, _, x, x]
We can make one bouquet of the first three flowers that bloomed. We cannot make another bouquet from the last three flowers that bloomed because they are not adjacent.
After day 12: [x, x, x, x, x, x, x]
It is obvious that we can make two bouquets in different ways.
```

 

__Constraints:__

*   `` bloomDay.length == n ``
*   <code>1 <= n <= 10<sup>5</sup></code>
*   <code>1 <= bloomDay[i] <= 10<sup>9</sup></code>
*   <code>1 <= m <= 10<sup>6</sup></code>
*   `` 1 <= k <= n ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 439,877 | 247,783 | 56.3% |