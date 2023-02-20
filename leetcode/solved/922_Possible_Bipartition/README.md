### [922. Possible Bipartition](https://leetcode.com/problems/possible-bipartition/)

Medium

We want to split a group of `` n `` people (labeled from `` 1 `` to `` n ``) into two groups of __any size__. Each person may dislike some other people, and they should not go into the same group.

Given the integer `` n `` and the array `` dislikes `` where <code>dislikes[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> indicates that the person labeled <code>a<sub>i</sub></code> does not like the person labeled <code>b<sub>i</sub></code>, return `` true `` _if it is possible to split everyone into two groups in this way_.

 

<strong class="example">Example 1:</strong>

```
Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: The first group has [1,4], and the second group has [2,3].
```

<strong class="example">Example 2:</strong>

```
Input: n = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
Explanation: We need at least 3 groups to divide them. We cannot put them in two groups.
```

 

__Constraints:__

*   `` 1 <= n <= 2000 ``
*   <code>0 <= dislikes.length <= 10<sup>4</sup></code>
*   `` dislikes[i].length == 2 ``
*   <code>1 <= a<sub>i</sub> < b<sub>i</sub> <= n</code>
*   All the pairs of `` dislikes `` are __unique__.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 354,327 | 176,951 | 49.9% |