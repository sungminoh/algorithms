### [956. Number of Music Playlists](https://leetcode.com/problems/number-of-music-playlists/description/)

Hard

Your music player contains `` n `` different songs. You want to listen to `` goal `` songs (not necessarily different) during your trip. To avoid boredom, you will create a playlist so that:

*   Every song is played __at least once__.
*   A song can only be played again only if `` k `` other songs have been played.

Given `` n ``, `` goal ``, and `` k ``, return _the number of possible playlists that you can create_. Since the answer can be very large, return it __modulo__ <code>10<sup>9</sup> + 7</code>.

 

<strong class="example">Example 1:</strong>

```
Input: n = 3, goal = 3, k = 1
Output: 6
Explanation: There are 6 possible playlists: [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], and [3, 2, 1].
```

<strong class="example">Example 2:</strong>

```
Input: n = 2, goal = 3, k = 0
Output: 6
Explanation: There are 6 possible playlists: [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2, 1], [2, 1, 2], and [1, 2, 2].
```

<strong class="example">Example 3:</strong>

```
Input: n = 2, goal = 3, k = 1
Output: 2
Explanation: There are 2 possible playlists: [1, 2, 1] and [2, 1, 2].
```

 

__Constraints:__

*   `` 0 <= k < n <= goal <= 100 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 113,991 | 68,986 | 60.5% |