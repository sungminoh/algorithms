### [935. Orderly Queue](https://leetcode.com/problems/orderly-queue/)

Hard

You are given a string `` s `` and an integer `` k ``. You can choose one of the first `` k `` letters of `` s `` and append it at the end of the string..

Return _the lexicographically smallest string you could have after applying the mentioned step any number of moves_.

 

__Example 1:__

```
Input: s = "cba", k = 1
Output: "acb"
Explanation: 
In the first move, we move the 1<sup>st</sup> character 'c' to the end, obtaining the string "bac".
In the second move, we move the 1<sup>st</sup> character 'b' to the end, obtaining the final result "acb".
```

__Example 2:__

```
Input: s = "baaca", k = 3
Output: "aaabc"
Explanation: 
In the first move, we move the 1<sup>st</sup> character 'b' to the end, obtaining the string "aacab".
In the second move, we move the 3<sup>rd</sup> character 'c' to the end, obtaining the final result "aaabc".
```

 

__Constraints:__

*   `` 1 <= k <= s.length <= 1000 ``
*   `` s `` consist of lowercase English letters.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 41,310 | 23,998 | 58.1% |