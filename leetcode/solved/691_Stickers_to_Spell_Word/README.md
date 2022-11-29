### [691. Stickers to Spell Word](https://leetcode.com/problems/stickers-to-spell-word/)

Hard

We are given `` n `` different types of `` stickers ``. Each sticker has a lowercase English word on it.

You would like to spell out the given string `` target `` by cutting individual letters from your collection of stickers and rearranging them. You can use each sticker more than once if you want, and you have infinite quantities of each sticker.

Return _the minimum number of stickers that you need to spell out _`` target ``. If the task is impossible, return `` -1 ``.

__Note:__ In all test cases, all words were chosen randomly from the `` 1000 `` most common US English words, and `` target `` was chosen as a concatenation of two random words.

 

<strong class="example">Example 1:</strong>

```
Input: stickers = ["with","example","science"], target = "thehat"
Output: 3
Explanation:
We can use 2 "with" stickers, and 1 "example" sticker.
After cutting and rearrange the letters of those stickers, we can form the target "thehat".
Also, this is the minimum number of stickers necessary to form the target string.
```

<strong class="example">Example 2:</strong>

```
Input: stickers = ["notice","possible"], target = "basicbasic"
Output: -1
Explanation:
We cannot form the target "basicbasic" from cutting letters from the given stickers.
```

 

__Constraints:__

*   `` n == stickers.length ``
*   `` 1 <= n <= 50 ``
*   `` 1 <= stickers[i].length <= 10 ``
*   `` 1 <= target.length <= 15 ``
*   `` stickers[i] `` and `` target `` consist of lowercase English letters.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 76,857 | 35,549 | 46.3% |