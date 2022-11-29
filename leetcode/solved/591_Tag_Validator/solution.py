#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string representing a code snippet, implement a tag validator to parse the code and return whether it is valid.

A code snippet is valid if all the following rules hold:

	The code must be wrapped in a valid closed tag. Otherwise, the code is invalid.
	A closed tag (not necessarily valid) has exactly the following format : TAG_CONTENT. Among them,  is the start tag, and  is the end tag. The TAG_NAME in start and end tags should be the same. A closed tag is valid if and only if the TAG_NAME and TAG_CONTENT are valid.
	A valid TAG_NAME only contain upper-case letters, and has length in range [1,9]. Otherwise, the TAG_NAME is invalid.
	A valid TAG_CONTENT may contain other valid closed tags, cdata and any characters (see note1) EXCEPT unmatched <, unmatched start and end tag, and unmatched or closed tags with invalid TAG_NAME. Otherwise, the TAG_CONTENT is invalid.
	A start tag is unmatched if no end tag exists with the same TAG_NAME, and vice versa. However, you also need to consider the issue of unbalanced when tags are nested.
	A < is unmatched if you cannot find a subsequent >. And when you find a < or </, all the subsequent characters until the next > should be parsed as TAG_NAME (not necessarily valid).
	The cdata has the following format : . The range of CDATA_CONTENT is defined as the characters between <![CDATA[ and the first subsequent ]]>.
	CDATA_CONTENT may contain any characters. The function of cdata is to forbid the validator to parse CDATA_CONTENT, so even it has some characters that can be parsed as tag (no matter valid or invalid), you should treat it as regular characters.

Example 1:

Input: code = "<DIV>This is the first line <![CDATA[<div>]]></DIV>"
Output: true
Explanation:
The code is wrapped in a closed tag : <DIV> and </DIV>.
The TAG_NAME is valid, the TAG_CONTENT consists of some characters and cdata.
Although CDATA_CONTENT has an unmatched start tag with invalid TAG_NAME, it should be considered as plain text, not parsed as a tag.
So TAG_CONTENT is valid, and then the code is valid. Thus return true.

Example 2:

Input: code = "<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>"
Output: true
Explanation:
We first separate the code into : start_tag|tag_content|end_tag.
start_tag -> "<DIV>"
end_tag -> "</DIV>"
tag_content could also be separated into : text1|cdata|text2.
text1 -> ">>  ![cdata[]] "
cdata -> "<![CDATA[<div>]>]]>", where the CDATA_CONTENT is "<div>]>"
text2 -> "]]>>]"
The reason why start_tag is NOT "<DIV>>>" is because of the rule 6.
The reason why cdata is NOT "<![CDATA[<div>]>]]>]]>" is because of the rule 7.

Example 3:

Input: code = "<A>  <B> </A>   </B>"
Output: false
Explanation: Unbalanced. If "<A>" is closed, then "<B>" must be unmatched, and vice versa.

Constraints:

	1 <= code.length <= 500
	code consists of English letters, digits, '<', '>', '/', '!', '[', ']', '.', and ' '.
"""
import pytest
import sys


class Solution:
    def isValid(self, code: str) -> bool:
        def get_tag(i):
            is_open = True
            if i+1 < len(code) and code[i+1] == '/':
                is_open = False
                i += 1
            i += 1
            j = code.find('>', i)
            tagname = code[i:j]
            valid = j>=0 and 1<=len(tagname)<=9 and all('A'<=c<='Z' for c in tagname)
            return j+1, tagname, is_open, valid

        i = 0
        stack = []
        while i < len(code):
            if code[i:].startswith('<![CDATA['):
                if not stack:
                    return False
                i = code.find(']]>', i)
                if i == -1:
                    return False
                i += 3
            elif code[i] == '<':
                i, tagname, is_open, valid = get_tag(i)
                if not valid:
                    return False
                if not is_open:
                    if stack and stack[-1] == tagname:
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(tagname)
            else:
                if not stack:
                    return False
                i += 1
            if not stack:
                break

        return len(stack) == 0 and i == len(code)


@pytest.mark.parametrize('code, expected', [
    ("<DIV>This is the first line <![CDATA[<div>]]></DIV>", True),
    ("<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>", True),
    ("<A>  <B> </A>   </B>", False),
    ("<DIV>This is the first line <![CDATA[<div>]]><DIV>", False),
    ("<![CDATA[wahaha]]]><![CDATA[]> wahaha]]>", False),
    ("<A></A><B></B>", False),
    ("<TRUE><![CDATA[wahaha]]]><![CDATA[]> wahaha]]></TRUE>", True),
    ("<A><A>/A></A></A>", True),
    ("<A><A></A></A>", True),
])
def test(code, expected):
    assert expected == Solution().isValid(code)

if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
