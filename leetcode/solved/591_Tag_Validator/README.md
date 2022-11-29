### [591. Tag Validator](https://leetcode.com/problems/tag-validator/)

Hard

Given a string representing a code snippet, implement a tag validator to parse the code and return whether it is valid.

A code snippet is valid if all the following rules hold:

1.   The code must be wrapped in a __valid closed tag__. Otherwise, the code is invalid.
2.   A __closed tag__ (not necessarily valid) has exactly the following format : `` <TAG_NAME>TAG_CONTENT</TAG_NAME> ``. Among them, `` <TAG_NAME> `` is the start tag, and `` </TAG_NAME> `` is the end tag. The TAG\_NAME in start and end tags should be the same. A closed tag is __valid__ if and only if the TAG\_NAME and TAG\_CONTENT are valid.
3.   A __valid__ `` TAG_NAME `` only contain __upper-case letters__, and has length in range \[1,9\]. Otherwise, the `` TAG_NAME `` is __invalid__.
4.   A __valid__ `` TAG_CONTENT `` may contain other __valid closed tags__, __cdata__ and any characters (see note1) __EXCEPT__ unmatched `` < ``, unmatched start and end tag, and unmatched or closed tags with invalid TAG\_NAME. Otherwise, the `` TAG_CONTENT `` is __invalid__.
5.   A start tag is unmatched if no end tag exists with the same TAG\_NAME, and vice versa. However, you also need to consider the issue of unbalanced when tags are nested.
6.   A `` < `` is unmatched if you cannot find a subsequent `` > ``. And when you find a `` < `` or `` </ ``, all the subsequent characters until the next `` > `` should be parsed as TAG\_NAME (not necessarily valid).
7.   The cdata has the following format : `` <![CDATA[CDATA_CONTENT]]> ``. The range of `` CDATA_CONTENT `` is defined as the characters between `` <![CDATA[ `` and the __first subsequent__ `` ]]> ``.
8.   `` CDATA_CONTENT `` may contain __any characters__. The function of cdata is to forbid the validator to parse `` CDATA_CONTENT ``, so even it has some characters that can be parsed as tag (no matter valid or invalid), you should treat it as __regular characters__.

 

<strong class="example">Example 1:</strong>

```
Input: code = "<DIV>This is the first line <![CDATA[<div>]]></DIV>"
Output: true
Explanation: 
The code is wrapped in a closed tag : <DIV> and </DIV>. 
The TAG_NAME is valid, the TAG_CONTENT consists of some characters and cdata. 
Although CDATA_CONTENT has an unmatched start tag with invalid TAG_NAME, it should be considered as plain text, not parsed as a tag.
So TAG_CONTENT is valid, and then the code is valid. Thus return true.
```

<strong class="example">Example 2:</strong>

```
Input: code = "<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>"
Output: true
Explanation:
We first separate the code into : start_tag|tag_content|end_tag.
start_tag -> <b>"<DIV>"</b>
end_tag -> <b>"</DIV>"</b>
tag_content could also be separated into : text1|cdata|text2.
text1 -> <b>">>  ![cdata[]] "</b>
cdata -> <b>"<![CDATA[<div>]>]]>"</b>, where the CDATA_CONTENT is <b>"<div>]>"</b>
text2 -> <b>"]]>>]"</b>
The reason why start_tag is NOT <b>"<DIV>>>"</b> is because of the rule 6.
The reason why cdata is NOT <b>"<![CDATA[<div>]>]]>]]>"</b> is because of the rule 7.
```

<strong class="example">Example 3:</strong>

```
Input: code = "<A>  <B> </A>   </B>"
Output: false
Explanation: Unbalanced. If "<A>" is closed, then "<B>" must be unmatched, and vice versa.
```

 

__Constraints:__

*   `` 1 <= code.length <= 500 ``
*   `` code `` consists of English letters, digits, `` '<' ``, `` '>' ``, `` '/' ``, `` '!' ``, `` '[' ``, `` ']' ``, `` '.' ``, and `` ' ' ``.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 33,690 | 12,516 | 37.2% |