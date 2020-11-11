#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an input string, reverse the string word by word.

Example:

Input: "the sky is blue",
Output: "blue is sky the".
Note:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.
Follow up: For C programmers, try to solve it in-place in O(1) space.
"""
class Solution(object):
    import re
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # trim and remove multiple whitespaces
        import re
        s = re.sub(r'\s+', ' ', s.strip())
        # return trivial case
        if not s:
            return ''

        lst = list(s)
        # reverse
        self.reverse(lst, 0, len(lst)-1)
        # reverse each word
        i = 0
        for j, c in enumerate(lst):
            if c == ' ':
                self.reverse(lst, i, j-1)
                i = j+1
        else:
            self.reverse(lst, i, j)
        return ''.join(lst)

    def reverse(self, lst, i, j):
        while i < j:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
            j -= 1


def main():
    s = input()
    print(Solution().reverseWords(s))


if __name__ == '__main__':
    main()
