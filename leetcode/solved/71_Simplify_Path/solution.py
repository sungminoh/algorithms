#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.

In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. For this problem, any other format of periods such as '...' are treated as file/directory names.

The canonical path should have the following format:

	The path starts with a single slash '/'.
	Any two directories are separated by a single slash '/'.
	The path does not end with a trailing '/'.
	The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')

Return the simplified canonical path.

Example 1:

Input: path = "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.

Example 2:

Input: path = "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.

Example 3:

Input: path = "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.

Constraints:

	1 <= path.length <= 3000
	path consists of English letters, digits, period '.', slash '/' or '_'.
	path is a valid absolute Unix path.
"""
import pytest
import sys


class Solution:
    def simplifyPath(self, path: str) -> str:
        """04/22/2018 06:10"""
        valid = []
        for p in filter(lambda x: x != '' and x != '.', path.split('/')):
            if p == '..':
                if valid:
                    valid.pop()
            else:
                valid.append(p)
        return '/' + '/'.join(valid)

    def simplifyPath(self, path: str) -> str:
        """Mar 27, 2022 15:18"""
        stack = []
        for d in path.split('/'):
            if d == '..':
                if stack:
                    stack.pop()
            elif d != '.' and d != '':
                stack.append(d)
        return '/' + '/'.join(stack)

    def simplifyPath(self, path: str) -> str:
        """"Sep 02, 2023 17:29"""
        stack = []
        for p in path.split('/'):
            if not p:
                continue
            if p == '..':
                if stack:
                    stack.pop()
            elif p == '.':
                pass  # no-op
            else:
                stack.append(p)
        while stack and not stack[-1]:
            stack.pop()
        return '/' + '/'.join(stack)


@pytest.mark.parametrize('args', [
    (("/home/", "/home")),
    (("/../", "/")),
    (("/home//foo/", "/home/foo")),
])
def test(args):
    assert args[-1] == Solution().simplifyPath(*args[:-1])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
