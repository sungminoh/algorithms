### [1777. Determine if Two Strings Are Close](https://leetcode.com/problems/determine-if-two-strings-are-close/)

Medium

Two strings are considered __close__ if you can attain one from the other using the following operations:

*   Operation 1: Swap any two __existing__ characters.	
    
    *   For example, <code>a<u>b</u>cd<u>e</u> -> a<u>e</u>cd<u>b</u></code>
    
    
    
*   Operation 2: Transform __every__ occurrence of one __existing__ character into another __existing__ character, and do the same with the other character.	
    
    *   For example, <code><u>aa</u>c<u>abb</u> -> <u>bb</u>c<u>baa</u></code> (all `` a ``'s turn into `` b ``'s, and all `` b ``'s turn into `` a ``'s)
    
    
    

You can use the operations on either string as many times as necessary.

Given two strings, `` word1 `` and `` word2 ``, return `` true ``_ if _`` word1 ``_ and _`` word2 ``_ are __close__, and _`` false ``_ otherwise._

 

<strong class="example">Example 1:</strong>

```
Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "a<u>bc</u>" -> "a<u>cb</u>"
Apply Operation 1: "<u>a</u>c<u>b</u>" -> "<u>b</u>c<u>a</u>"
```

<strong class="example">Example 2:</strong>

```
Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.
```

<strong class="example">Example 3:</strong>

<strong>Input:</strong> word1 = "cabbba", word2 = "abbccc"
    <strong>Output:</strong> true
    <strong>Explanation:</strong> You can attain word2 from word1 in 3 operations.
    Apply Operation 1: "ca<u>b</u>bb<u>a</u>" -> "ca<u>a</u>bb<u>b</u>"
    Apply Operation 2: "<u>c</u>aa<u>bbb</u>" -> "<u>b</u>aa<u>ccc</u>"
    Apply Operation 2: "<u>baa</u>ccc" -> "<u>abb</u>ccc"

 

__Constraints:__

*   <code>1 <= word1.length, word2.length <= 10<sup>5</sup></code>
*   `` word1 `` and `` word2 `` contain only lowercase English letters.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 174,040 | 98,418 | 56.5% |