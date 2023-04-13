### [907. Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/)

Medium

Koko loves to eat bananas. There are `` n `` piles of bananas, the <code>i<sup>th</sup></code> pile has `` piles[i] `` bananas. The guards have gone and will come back in `` h `` hours.

Koko can decide her bananas-per-hour eating speed of `` k ``. Each hour, she chooses some pile of bananas and eats `` k `` bananas from that pile. If the pile has less than `` k `` bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return _the minimum integer_ `` k `` _such that she can eat all the bananas within_ `` h `` _hours_.

 

<strong class="example">Example 1:</strong>

```
Input: piles = [3,6,7,11], h = 8
Output: 4
```

<strong class="example">Example 2:</strong>

```
Input: piles = [30,11,23,4,20], h = 5
Output: 30
```

<strong class="example">Example 3:</strong>

```
Input: piles = [30,11,23,4,20], h = 6
Output: 23
```

 

__Constraints:__

*   <code>1 <= piles.length <= 10<sup>4</sup></code>
*   <code>piles.length <= h <= 10<sup>9</sup></code>
*   <code>1 <= piles[i] <= 10<sup>9</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 669,398 | 349,007 | 52.1% |