#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a C++ program, remove comments from it. The program source is an array where source[i] is the i-th line of the source code.  This represents the result of splitting the original source code string by the newline character \n.

In C++, there are two types of comments, line comments, and block comments.

The string // denotes a line comment, which represents that it and rest of the characters to the right of it in the same line should be ignored.

The string /* denotes a block comment, which represents that all characters until the next (non-overlapping) occurrence of */ should be ignored.  (Here, occurrences happen in reading order: line by line from left to right.)  To be clear, the string /*/ does not yet end the block comment, as the ending would be overlapping the beginning.

The first effective comment takes precedence over others: if the string // occurs in a block comment, it is ignored. Similarly, if the string /* occurs in a line or block comment, it is also ignored.

If a certain line of code is empty after removing comments, you must not output that line: each string in the answer list will be non-empty.

There will be no control characters, single quote, or double quote characters.  For example, source = "string s = "/* Not a comment. */";" will not be a test case.  (Also, nothing else such as defines or macros will interfere with the comments.)

It is guaranteed that every open block comment will eventually be closed, so /* outside of a line or block comment always starts a new comment.

Finally, implicit newline characters can be deleted by block comments.  Please see the examples below for details.

After removing the comments from the source code, return the source code in the same format.

Example 1:

Input:
source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]

The line by line code is visualized as below:
/*Test program */
int main()
{
  // variable declaration
int a, b, c;
/* This is a test
   multiline
   comment for
   testing */
a = b + c;
}

Output: ["int main()","{ ","  ","int a, b, c;","a = b + c;","}"]

The line by line code is visualized as below:
int main()
{

int a, b, c;
a = b + c;
}

Explanation:
The string /* denotes a block comment, including line 1 and lines 6-9. The string // denotes line 4 as comments.

Example 2:

Input:
source = ["a/*comment", "line", "more_comment*/b"]
Output: ["ab"]
Explanation: The original source string is "a/*comment\nline\nmore_comment*/b", where we have bolded the newline characters.  After deletion, the implicit newline characters are deleted, leaving the string "ab", which when delimited by newline characters becomes ["ab"].

Note:
The length of source is in the range [1, 100].
The length of source[i] is in the range [0, 80].
Every open block comment is eventually closed.
There are no single-quote, double-quote, or control characters in the source code.
"""
import sys
import re
from typing import List
import pytest


class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ret = []
        started = False
        for line in source:
            i = 0
            if not started:
                l = []
            while i < len(line):
                if started:
                    if line[i:min(len(line), i+2)] == '*/':
                        i += 1
                        started = False
                else:
                    if line[i:min(len(line), i+2)] == '/*':
                        i += 1
                        started = True
                    elif line[i:min(len(line), i+2)] == '//':
                        break
                    else:
                        l.append(line[i])
                i += 1
            if not started and l:
                ret.append(''.join(l))
        return ret

    def _removeComments(self, source: List[str]) -> List[str]:
        ret = []
        started = False
        for line in source:
            slash = line.find('//')
            star = line.find('/*')
            starc = line.find('*/', (star+2) if star >= 0 else 0)
            if not started:
                if star >= 0 and (slash < 0 or slash > star):
                    started = True
                starts = [x for x in [star, slash] if x >= 0]
                start = min(starts) if starts else None
                ret.append(line[:start])
            if started and starc >= max(0, star+2):
                started = False
                end = slash if slash > starc else None
                ret[-1] += line[starc+2:end]
        return [x for x in ret if len(x) > 0]

    def _removeComments(self, source: List[str]) -> List[str]:
        s = re.sub(r'/\*.*?\*/', '', '\n'.join(source), flags=re.DOTALL)
        s = re.sub(r'//.*', '', s)
        return [x for x in s.split('\n') if len(x) > 0]



@pytest.mark.parametrize('source, expected', [
    (["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"],
     ["int main()","{ ","  ","int a, b, c;","a = b + c;","}"]),
    (["a/*comment", "line", "more_comment*/b"], ["ab"]),
    (["void func(int k) {", "// this function does nothing /*", "   k = k*2/4;", "   k = k/2;*/", "}"],
     ["void func(int k) {","   k = k*2/4;","   k = k/2;*/","}"]),
    (["main() {", "/* here is commments", "  // still comments */", "   double s = 33;", "   cout << s;", "}"],
     ["main() {","   double s = 33;","   cout << s;","}"]),
    (["main() {", "  Node* p;", "  /* declare a Node", "  /*float f = 2.0", "   p->val = f;", "   /**/", "   p->val = 1;", "   //*/ cout << success;*/", "}", " "],
     ["main() {","  Node* p;","  ","   p->val = 1;","   ","}"," "]),
    (["struct Node{", "    /*/ declare members;/**/", "    int size;", "    /**/int val;", "};"],
     ["struct Node{","    ","    int size;","    int val;","};"]),
    (["a//*b//*c","blank","d/*/e*//f"], ["a","blank","d/f"])
])
def test(source, expected):
    actual = Solution().removeComments(source)
    print()
    print('\n'.join(source))
    print('----------------------')
    print('\n'.join(actual))
    print('----------------------')
    print('\n'.join(expected))
    assert expected == actual


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
