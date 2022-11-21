### [151. Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/)

Medium

Given an input string `` s ``, reverse the order of the __words__.

A __word__ is defined as a sequence of non-space characters. The __words__ in `` s `` will be separated by at least one space.

Return _a string of the words in reverse order concatenated by a single space._

__Note__ that `` s `` may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

<strong class="example">Example 1:</strong>

```
Input: s = "the sky is blue"
Output: "blue is sky the"
```

<strong class="example">Example 2:</strong>

```
Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
```

<strong class="example">Example 3:</strong>

```
Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
```

 

__Constraints:__

*   <code>1 <= s.length <= 10<sup>4</sup></code>
*   `` s `` contains English letters (upper-case and lower-case), digits, and spaces `` ' ' ``.
*   There is __at least one__ word in `` s ``.

 

<b data-stringify-type="bold">Follow-up: </b>If the string data type is mutable in your language, can you solve it <b data-stringify-type="bold">in-place</b> with <code data-stringify-type="code">O(1)</code> extra space?

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 2,693,561 | 856,363 | 31.8% |