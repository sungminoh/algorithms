
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Suppose we abstract our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext

The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext

The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the length of the longest absolute path to file in the abstracted file system. If there is no file in the system, return 0.

Note:

The name of a file contains at least a . and an extension.
The name of a directory or sub-directory will not contain a ..

Time complexity required: O(n) where n is the size of the input string.

Notice that a/aa/aaa/file1.txt is not the longest file path, if there is another path aaaaaaaaaaaaaaaaaaaaa/sth.png.
"""
from collections import defaultdict
import pytest


class Solution:
    def lengthLongestPath(self, input: str) -> int:
        def _rec(structure):
            if not structure:
                return 0
            path = ''
            m = 0
            for k, substructures in structure.items():
                if not substructures and '.' in k and len(k) > m:
                    m = len(k)
                    path = k
                for substructure in substructures:
                    length = len(k)
                    current_path = k
                    subsize, subpath = _rec(substructure)
                    if subsize:
                        length += subsize + 1
                        current_path += '/' + subpath
                        if length > m:
                            m = length
                            path = current_path
            # print(structure, m, path)
            return m, path
        structures = self.deserialize(input)
        return max(_rec(structure)[0] for structure in structures)

    def deserialize(self, s):
        def _next_prefix(prefix):
            if not prefix:
                return '\n\t'
            else:
                return prefix + '\t'

        def _cut_word(i):
            j = i
            while j < len(s) and s[j] in {'\t', '\n'}:
                j += 1
            while j < len(s) and s[j] != '\n':
                j += 1
            return s[i:j], j

        def _common_prefix(prefix, i):
            j = 0
            orig_i = i
            # print('%r, %r' % (prefix, s[i:]))
            while j < len(prefix) and (prefix[j] == s[i] or (prefix[j] == '\t' and s[i:i+4]) == '    '):
                i += 1 if prefix[j] == s[i] else 4
                j += 1
            # print('%r, %r' % (prefix[:j], i - orig_i))
            return prefix[:j], i - orig_i

        def _rec(i, prefix=''):
            while i < len(s) and i == '\n':
                i += 1
            # print('s: %r, prefix: %r' % (s[i:], prefix))
            _prefix, used = _common_prefix(prefix, i)
            if prefix and prefix != _prefix:
                return None, i
            word, j = _cut_word(i + used)
            # j = i + len(prefix) + len(word)

            next_prefix = _next_prefix(prefix)
            ret = []
            while j < len(s):
                sub, j = _rec(j, next_prefix)
                if not sub:
                    break
                ret.append(sub)
            return {word: ret}, j

        # ret = []
        j = 0
        while j < len(s):
            print(j)
            structure, j = _rec(j)
            j += 1
            if structure:
                yield structure
                # ret.append(structure)
        # return ret


@pytest.mark.parametrize('s, expected', [
    ('dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext', 32),
    ('a', 0),
    ("a\n\tb\n\t\tc", 0),
    ("dir\n\tfile.txt", 12),
    ("dir\n    file.txt", 12),
    ("dir\n        file.txt", 16),
    ("a\n\tb.txt\na2\n\tb2.txt", 9)
])
def test(s, expected):
    assert expected == Solution().lengthLongestPath(s)
