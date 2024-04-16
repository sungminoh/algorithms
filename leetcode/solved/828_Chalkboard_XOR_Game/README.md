### [828. Chalkboard XOR Game](https://leetcode.com/problems/chalkboard-xor-game/description/)

Hard

You are given an array of integers `` nums `` represents the numbers written on a chalkboard.

Alice and Bob take turns erasing exactly one number from the chalkboard, with Alice starting first. If erasing a number causes the bitwise XOR of all the elements of the chalkboard to become `` 0 ``, then that player loses. The bitwise XOR of one element is that element itself, and the bitwise XOR of no elements is `` 0 ``.

Also, if any player starts their turn with the bitwise XOR of all the elements of the chalkboard equal to `` 0 ``, then that player wins.

Return `` true `` _if and only if Alice wins the game, assuming both players play optimally_.

 

<strong class="example">Example 1:</strong>

```
Input: nums = [1,1,2]
Output: false
Explanation: 
Alice has two choices: erase 1 or erase 2. 
If she erases 1, the nums array becomes [1, 2]. The bitwise XOR of all the elements of the chalkboard is 1 XOR 2 = 3. Now Bob can remove any element he wants, because Alice will be the one to erase the last element and she will lose. 
If Alice erases 2 first, now nums become [1, 1]. The bitwise XOR of all the elements of the chalkboard is 1 XOR 1 = 0. Alice will lose.
```

<strong class="example">Example 2:</strong>

```
Input: nums = [0,1]
Output: true
```

<strong class="example">Example 3:</strong>

```
Input: nums = [1,2,3]
Output: true
```

 

__Constraints:__

*   `` 1 <= nums.length <= 1000 ``
*   <code>0 <= nums[i] < 2<sup>16</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 17,788 | 10,527 | 59.2% |