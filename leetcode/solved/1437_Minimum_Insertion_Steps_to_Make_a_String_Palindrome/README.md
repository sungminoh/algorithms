### [1437. Minimum Insertion Steps to Make a String Palindrome](https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/?envType=daily-question&envId=2023-04-22)

Hard

Given a string `` s ``. In one step you can insert any character at any index of the string.

Return _the minimum number of steps_ to make `` s `` palindrome.

A __Palindrome String__ is one that reads the same backward as well as forward.

 

<strong class="example">Example 1:</strong>

```
Input: s = "zzazz"
Output: 0
Explanation: The string "zzazz" is already palindrome we do not need any insertions.
```

<strong class="example">Example 2:</strong>

```
Input: s = "mbadm"
Output: 2
Explanation: String can be "mbdadbm" or "mdbabdm".
```

<strong class="example">Example 3:</strong>

```
Input: s = "leetcode"
Output: 5
Explanation: Inserting 5 characters the string becomes "leetcodocteel".
```

 

__Constraints:__

*   `` 1 <= s.length <= 500 ``
*   `` s `` consists of lowercase English letters.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 198,879 | 138,746 | 69.8% |