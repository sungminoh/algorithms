### [2123. The Number of Weak Characters in the Game](https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/)

Medium

You are playing a game that contains multiple characters, and each of the characters has __two__ main properties: __attack__ and __defense__. You are given a 2D integer array `` properties `` where <code>properties[i] = [attack<sub>i</sub>, defense<sub>i</sub>]</code> represents the properties of the <code>i<sup>th</sup></code> character in the game.

A character is said to be __weak__ if any other character has __both__ attack and defense levels __strictly greater__ than this character's attack and defense levels. More formally, a character `` i `` is said to be __weak__ if there exists another character `` j `` where <code>attack<sub>j</sub> > attack<sub>i</sub></code> and <code>defense<sub>j</sub> > defense<sub>i</sub></code>.

Return _the number of __weak__ characters_.

 

__Example 1:__

```
Input: properties = [[5,5],[6,3],[3,6]]
Output: 0
Explanation: No character has strictly greater attack and defense than the other.
```

__Example 2:__

```
Input: properties = [[2,2],[3,3]]
Output: 1
Explanation: The first character is weak because the second character has a strictly greater attack and defense.
```

__Example 3:__

```
Input: properties = [[1,5],[10,4],[4,3]]
Output: 1
Explanation: The third character is weak because the second character has a strictly greater attack and defense.
```

 

__Constraints:__

*   <code>2 <= properties.length <= 10<sup>5</sup></code>
*   `` properties[i].length == 2 ``
*   <code>1 <= attack<sub>i</sub>, defense<sub>i</sub> <= 10<sup>5</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 193,793 | 85,050 | 43.9% |