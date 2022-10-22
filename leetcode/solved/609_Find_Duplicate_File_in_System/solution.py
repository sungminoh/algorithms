#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a list paths of directory info, including the directory path, and all the files with contents in this directory, return all the duplicate files in the file system in terms of their paths. You may return the answer in any order.

A group of duplicate files consists of at least two files that have the same content.

A single directory info string in the input list has the following format:

	"root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)"

It means there are n files (f1.txt, f2.txt ... fn.txt) with content (f1_content, f2_content ... fn_content) respectively in the directory "root/d1/d2/.../dm". Note that n >= 1 and m >= 0. If m = 0, it means the directory is just the root directory.

The output is a list of groups of duplicate file paths. For each group, it contains all the file paths of the files that have the same content. A file path is a string that has the following format:

	"directory_path/file_name.txt"

Example 1:
Input: paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
Output: [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]
Example 2:
Input: paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"]
Output: [["root/a/2.txt","root/c/d/4.txt"],["root/a/1.txt","root/c/3.txt"]]

Constraints:

	1 <= paths.length <= 2 * 104
	1 <= paths[i].length <= 3000
	1 <= sum(paths[i].length) <= 5 * 105
	paths[i] consist of English letters, digits, '/', '.', '(', ')', and ' '.
	You may assume no files or directories share the same name in the same directory.
	You may assume each given directory info represents a unique directory. A single blank space separates the directory path and file info.

Follow up:

	Imagine you are given a real file system, how will you search files? DFS or BFS?
	If the file content is very large (GB level), how will you modify your solution?
	If you can only read the file by 1kb each time, how will you modify your solution?
	What is the time complexity of your modified solution? What is the most time-consuming part and memory-consuming part of it? How to optimize?
	How to make sure the duplicated files you find are not false positive?
"""
import os
from collections import defaultdict
from typing import List
import pytest
import sys


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        """06/14/2020 16:49"""
        groups = defaultdict(list)
        for path in paths:
            d, *files = path.split()
            for fc in files:
                f, c = fc[:-1].split('(')
                groups[c].append(f'{d}/{f}')
        return list(x for x in groups.values() if len(x) > 1)

    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        """06/02/2021 06:39
        Imagine you are given a real file system, how will you search files? DFS or BFS?
        - Either would work. But I'd use DFS not to keep a queue
        If the file content is very large (GB level), how will you modify your solution?
        - Leverage file size first and read some part of file and run recursively.
        If you can only read the file by 1kb each time, how will you modify your solution?
        - Make a recursive call to each group reading next 1kb
        What is the time complexity of your modified solution? What is the most time-consuming part and memory-consuming part of it? How to optimize?
        - O(n*filesize)
        How to make sure the duplicated files you find are not false positive?
        - Make sure to see all file content
        """
        groups = defaultdict(list)
        for path in paths:
            d, *fs = path.split(' ')
            for f in fs:
                n, c = f[:-1].split('(')
                groups[c].append(d + '/' + n)
        return [x for x in groups.values() if len(x) > 1]


    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for path in paths:
            d, *files = path.split(' ')
            for f in files:
                fname, content = f[:-1].split('(')
                groups[content].append(os.path.join(d, fname))
        return [x for x in groups.values() if len(x)>=2]


@pytest.mark.parametrize('paths, expected', [
    (["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"], [["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]),
    (["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"], [["root/a/2.txt","root/c/d/4.txt"],["root/a/1.txt","root/c/3.txt"]]),
    (["root/a 1.txt(abcd) 2.txt(efsfgh)","root/c 3.txt(abdfcd)","root/c/d 4.txt(efggdfh)"], [])
])
def test(paths, expected):
    actual = Solution().findDuplicate(paths)
    assert sorted([sorted(x) for x in expected]) == sorted([sorted(x) for x in actual])


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
