### [940. Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/)

Medium

You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array `` fruits `` where `` fruits[i] `` is the __type__ of fruit the <code>i<sup>th</sup></code> tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

*   You only have __two__ baskets, and each basket can only hold a __single type__ of fruit. There is no limit on the amount of fruit each basket can hold.
*   Starting from any tree of your choice, you must pick __exactly one fruit__ from __every__ tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
*   Once you reach a tree with fruit that cannot fit in your baskets, you must stop.

Given the integer array `` fruits ``, return _the __maximum__ number of fruits you can pick_.

 

<strong class="example">Example 1:</strong>

```
Input: fruits = [<u>1,2,1</u>]
Output: 3
Explanation: We can pick from all 3 trees.
```

<strong class="example">Example 2:</strong>

```
Input: fruits = [0,<u>1,2,2</u>]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].
```

<strong class="example">Example 3:</strong>

```
Input: fruits = [1,<u>2,3,2,2</u>]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].
```

 

__Constraints:__

*   <code>1 <= fruits.length <= 10<sup>5</sup></code>
*   `` 0 <= fruits[i] < fruits.length ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 748,840 | 327,449 | 43.7% |