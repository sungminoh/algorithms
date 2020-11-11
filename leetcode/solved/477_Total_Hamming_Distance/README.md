### [477. Total Hamming Distance](https://leetcode.com/problems/total-hamming-distance/)

Medium

The <a href="https://en.wikipedia.org/wiki/Hamming_distance" target="_blank">Hamming distance</a> between two integers is the number of positions at which the corresponding bits are different.

Now your job is to find the total Hamming distance between all pairs of the given numbers.

__Example:__  

```
<b>Input:</b> 4, 14, 2

<b>Output:</b> 6

<b>Explanation:</b> In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
showing the four bits relevant in this case). So the answer will be:
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.
```

__Note:__  

1.   Elements of the given array are in the range of `` 0  `` to `` 10^9 ``<li>Length of the array will not exceed <code>10^4</code>. </li>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 119,498 | 60,072 | 50.3% |