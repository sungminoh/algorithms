### [390. Elimination Game](https://leetcode.com/problems/elimination-game/)

Medium

There is a list of sorted integers from 1 to _n_. Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.

Repeat the previous step again, but this time from right to left, remove the right most number and every other number from the remaining numbers.

We keep repeating the steps again, alternating left to right and right to left, until a single number remains.

Find the last number that remains starting with a list of length _n_.

__Example:__

```
Input:
n = 9,
<u>1</u> 2 <u>3</u> 4 <u>5</u> 6 <u>7</u> 8 <u>9</u>
2 <u>4</u> 6 <u>8</u>
<u>2</u> 6
6

Output:
6
```

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 68,091 | 30,138 | 44.3% |