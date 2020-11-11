### [648. Replace Words](https://leetcode.com/problems/replace-words/)

Medium

In English, we have a concept called `` root ``, which can be followed by some other words to form another longer word - let's call this word `` successor ``. For example, the root `` an ``, followed by `` other ``, which can form another word `` another ``.

Now, given a dictionary consisting of many roots and a sentence. You need to replace all the `` successor `` in the sentence with the `` root `` forming it. If a `` successor `` has many `` roots `` can form it, replace it with the root with the shortest length.

You need to output the sentence after the replacement.

 

__Example 1:__

```
Input: dict = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
```

 

__Constraints:__

*   The input will only have lower-case letters.
*   `` 1 <= dict.length <= 1000 ``
*   `` 1 <= dict[i].length <= 100 ``
*   1 <= sentence words number <= 1000
*   1 <= sentence words length <= 1000

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 95,256 | 53,409 | 56.1% |