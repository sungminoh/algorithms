### [676. Implement Magic Dictionary](https://leetcode.com/problems/implement-magic-dictionary/)

Medium

Implement a magic directory with `` buildDict ``, and `` search `` methods.

For the method `` buildDict ``, you'll be given a list of non-repetitive words to build a dictionary.

For the method `` search ``, you'll be given a word, and judge whether if you modify __exactly__ one character into __another__ character in this word, the modified word is in the dictionary you just built.

__Example 1:__  

```
Input: buildDict(["hello", "leetcode"]), Output: Null
Input: search("hello"), Output: False
Input: search("hhllo"), Output: True
Input: search("hell"), Output: False
Input: search("leetcoded"), Output: False
```

__Note:__  

1.   You may assume that all the inputs are consist of lowercase letters `` a-z ``.
2.   For contest purpose, the test data is rather small by now. You could think about highly efficient algorithm after the contest.
3.   Please remember to __RESET__ your class variables declared in class MagicDictionary, as static/class variables are __persisted across multiple test cases__. Please see [here](https://leetcode.com/faq/#different-output) for more details.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 75,306 | 41,051 | 54.5% |