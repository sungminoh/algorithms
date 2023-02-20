### [2094. Remove Stones to Minimize the Total](https://leetcode.com/problems/remove-stones-to-minimize-the-total/)

Medium

You are given a __0-indexed__ integer array `` piles ``, where `` piles[i] `` represents the number of stones in the <code>i<sup>th</sup></code> pile, and an integer `` k ``. You should apply the following operation __exactly__ `` k `` times:

*   Choose any `` piles[i] `` and __remove__ `` floor(piles[i] / 2) `` stones from it.

__Notice__ that you can apply the operation on the __same__ pile more than once.

Return _the __minimum__ possible total number of stones remaining after applying the _`` k ``_ operations_.

`` floor(x) `` is the __greatest__ integer that is __smaller__ than or __equal__ to `` x `` (i.e., rounds `` x `` down).

 

<strong class="example">Example 1:</strong>

```
Input: piles = [5,4,9], k = 2
Output: 12
Explanation: Steps of a possible scenario are:
- Apply the operation on pile 2. The resulting piles are [5,4,<u>5</u>].
- Apply the operation on pile 0. The resulting piles are [<u>3</u>,4,5].
The total number of stones in [3,4,5] is 12.
```

<strong class="example">Example 2:</strong>

```
Input: piles = [4,3,6,7], k = 3
Output: 12
Explanation: Steps of a possible scenario are:
- Apply the operation on pile 2. The resulting piles are [4,3,<u>3</u>,7].
- Apply the operation on pile 3. The resulting piles are [4,3,3,<u>4</u>].
- Apply the operation on pile 0. The resulting piles are [<u>2</u>,3,3,4].
The total number of stones in [2,3,3,4] is 12.
```

 

__Constraints:__

*   <code>1 <= piles.length <= 10<sup>5</sup></code>
*   <code>1 <= piles[i] <= 10<sup>4</sup></code>
*   <code>1 <= k <= 10<sup>5</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 127,495 | 76,563 | 60.1% |