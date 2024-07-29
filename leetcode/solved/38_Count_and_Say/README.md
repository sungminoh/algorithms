### [38. Count and Say](https://leetcode.com/problems/count-and-say/description/)

Medium

The __count-and-say__ sequence is a sequence of digit strings defined by the recursive formula:

*   `` countAndSay(1) = "1" ``
*   `` countAndSay(n) `` is the run-length encoding of `` countAndSay(n - 1) ``.

<a href="http://en.wikipedia.org/wiki/Run-length_encoding" target="_blank">Run-length encoding</a> (RLE) is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string `` "3322251" `` we replace `` "33" `` with `` "23" ``, replace `` "222" `` with `` "32" ``, replace `` "5" `` with `` "15" `` and replace `` "1" `` with `` "11" ``. Thus the compressed string becomes `` "23321511" ``.

Given a positive integer `` n ``, return _the _<code>n<sup>th</sup></code>_ element of the __count-and-say__ sequence_.

 

<strong class="example">Example 1:</strong>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 4</span></p>
<p><strong>Output:</strong> <span class="example-io">"1211"</span></p>
<p><strong>Explanation:</strong></p>
```
countAndSay(1) = "1"
countAndSay(2) = RLE of "1" = "11"
countAndSay(3) = RLE of "11" = "21"
countAndSay(4) = RLE of "21" = "1211"
```
</div>

<strong class="example">Example 2:</strong>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 1</span></p>
<p><strong>Output:</strong> <span class="example-io">"1"</span></p>
<p><strong>Explanation:</strong></p>
<p>This is the base case.</p>
</div>

 

__Constraints:__

*   `` 1 <= n <= 30 ``

 
__Follow up:__ Could you solve it iteratively?

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 1,705,153 | 948,038 | 55.6% |