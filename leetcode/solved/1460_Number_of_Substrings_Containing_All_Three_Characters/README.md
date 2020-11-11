### [1460. Number of Substrings Containing All Three Characters](https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/)

Medium

Given a string `` s `` consisting only of characters _a_, _b_ and _c_.

Return the number of substrings containing __at least__ one occurrence of all these characters _a_, _b_ and _c_.

 

__Example 1:__

```
Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters <em>a</em>, <em>b</em> and <em>c are "</em>abc<em>", "</em>abca<em>", "</em>abcab<em>", "</em>abcabc<em>", "</em>bca<em>", "</em>bcab<em>", "</em>bcabc<em>", "</em>cab<em>", "</em>cabc<em>" </em>and<em> "</em>abc<em>" </em>(again)<em>. </em>
```

__Example 2:__

```
Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters <em>a</em>, <em>b</em> and <em>c are "</em>aaacb<em>", "</em>aacb<em>" </em>and<em> "</em>acb<em>".</em><em> </em>
```

__Example 3:__

```
Input: s = "abc"
Output: 1
```

 

__Constraints:__

*   `` 3 <= s.length <= 5 x 10^4 ``
*   `` s `` only consists of _a_, _b_ or _c _characters.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 25,464 | 15,284 | 60.0% |