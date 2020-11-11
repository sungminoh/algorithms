### [529. Minesweeper](https://leetcode.com/problems/minesweeper/)

Medium

Let's play the minesweeper game ([Wikipedia](https://en.wikipedia.org/wiki/Minesweeper_(video_game)), [online game](http://minesweeperonline.com))!

You are given a 2D char matrix representing the game board. __'M'__ represents an __unrevealed__ mine, __'E'__ represents an __unrevealed__ empty square, __'B'__ represents a __revealed__ blank square that has no adjacent (above, below, left, right, and all 4 diagonals) mines, __digit__ ('1' to '8') represents how many mines are adjacent to this __revealed__ square, and finally __'X'__ represents a __revealed__ mine.

Now given the next click position (row and column indices) among all the __unrevealed__ squares ('M' or 'E'), return the board after revealing this position according to the following rules:

1.   If a mine ('M') is revealed, then the game is over - change it to __'X'__.
2.   If an empty square ('E') with __no adjacent mines__ is revealed, then change it to revealed blank ('B') and all of its adjacent __unrevealed__ squares should be revealed recursively.
3.   If an empty square ('E') with __at least one adjacent mine__ is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
4.   Return the board when no more squares will be revealed.

 

__Example 1:__

```
<b>Input:</b> 

[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

Click : [3,0]

<b>Output:</b> 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

<b>Explanation:</b>
<img src="https://assets.leetcode.com/uploads/2018/10/12/minesweeper_example_1.png" style="width: 100%; max-width: 400px"/>
```

__Example 2:__

```
<b>Input:</b> 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

Click : [1,2]

<b>Output:</b> 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'X', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]

<b>Explanation:</b>
<img src="https://assets.leetcode.com/uploads/2018/10/12/minesweeper_example_2.png" style="width: 100%; max-width: 400px"/>
```

 

__Note:__

1.   The range of the input matrix's height and width is \[1,50\].
2.   The click position will only be an unrevealed square ('M' or 'E'), which also means the input board contains at least one clickable square.
3.   The input board won't be a stage when game is over (some mines have been revealed).
4.   For simplicity, not mentioned rules should be ignored in this problem. For example, you __don't__ need to reveal all the unrevealed mines when the game is over, consider any cases that you will win the game or flag any squares.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 100,338 | 58,438 | 58.2% |