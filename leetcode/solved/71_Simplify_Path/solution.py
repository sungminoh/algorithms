#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 sungmin <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"

Corner Cases:

Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".
"""


class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        valid = []
        for p in filter(lambda x: x != '' and x != '.', path.split('/')):
            if p == '..':
                if valid:
                    valid.pop()
            else:
                valid.append(p)
        return '/' + '/'.join(valid)


def main():
    print(Solution().simplifyPath(input()))


if __name__ == '__main__':
    main()
