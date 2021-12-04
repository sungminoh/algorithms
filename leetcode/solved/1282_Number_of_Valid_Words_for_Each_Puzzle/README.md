### [1282. Number of Valid Words for Each Puzzle](https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/)

Hard

With respect to a given `` puzzle `` string, a `` word `` is _valid_ if both the following conditions are satisfied:

*   `` word `` contains the first letter of `` puzzle ``.
*   For each letter in `` word ``, that letter is in `` puzzle ``.	
    
    *   For example, if the puzzle is `` "abcdefg" ``, then valid words are `` "faced" ``, `` "cabbage" ``, and `` "baggage" ``, while
    *   invalid words are `` "beefed" `` (does not include `` 'a' ``) and `` "based" `` (includes `` 's' `` which is not in the puzzle).
    
    
    

Return _an array _`` answer ``_, where _`` answer[i] ``_ is the number of words in the given word list _`` words ``_ that is valid with respect to the puzzle _`` puzzles[i] ``.
 

__Example 1:__

```
Input: words = ["aaaa","asas","able","ability","actt","actor","access"], puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
Output: [1,1,3,2,4,0]
Explanation: 
1 valid word for "aboveyz" : "aaaa" 
1 valid word for "abrodyz" : "aaaa"
3 valid words for "abslute" : "aaaa", "asas", "able"
2 valid words for "absoryz" : "aaaa", "asas"
4 valid words for "actresz" : "aaaa", "asas", "actt", "access"
There are no valid words for "gaswxyz" cause none of the words in the list contains letter 'g'.
```

__Example 2:__

```
Input: words = ["apple","pleas","please"], puzzles = ["aelwxyz","aelpxyz","aelpsxy","saelpxy","xaelpsy"]
Output: [0,1,3,2,0]
```

 

__Constraints:__

*   <code>1 <= words.length <= 10<sup>5</sup></code>
*   `` 4 <= words[i].length <= 50 ``
*   <code>1 <= puzzles.length <= 10<sup>4</sup></code>
*   `` puzzles[i].length == 7 ``
*   `` words[i] `` and `` puzzles[i] `` consist of lowercase English letters.
*   Each `` puzzles[i]  ``does not contain repeated characters.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 53,551 | 25,091 | 46.9% |