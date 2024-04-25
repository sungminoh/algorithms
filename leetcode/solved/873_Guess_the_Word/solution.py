#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
You are given an array of unique strings words where words[i] is six letters long. One word of words was chosen as a secret word.

You are also given the helper object Master. You may call Master.guess(word) where word is a six-letter-long string, and it must be from words. Master.guess(word) returns:

	-1 if word is not from words, or
	an integer representing the number of exact matches (value and position) of your guess to the secret word.

There is a parameter allowedGuesses for each test case where allowedGuesses is the maximum number of times you can call Master.guess(word).

For each test case, you should call Master.guess with the secret word without exceeding the maximum number of allowed guesses. You will get:

	"Either you took too many guesses, or you did not find the secret word." if you called Master.guess more than allowedGuesses times or if you did not call Master.guess with the secret word, or
	"You guessed the secret word correctly." if you called Master.guess with the secret word with the number of calls to Master.guess less than or equal to allowedGuesses.

The test cases are generated such that you can guess the secret word with a reasonable strategy (other than using the bruteforce method).

Example 1:

Input: secret = "acckzz", words = ["acckzz","ccbazz","eiowzz","abcczz"], allowedGuesses = 10
Output: You guessed the secret word correctly.
Explanation:
master.guess("aaaaaa") returns -1, because "aaaaaa" is not in wordlist.
master.guess("acckzz") returns 6, because "acckzz" is secret and has all 6 matches.
master.guess("ccbazz") returns 3, because "ccbazz" has 3 matches.
master.guess("eiowzz") returns 2, because "eiowzz" has 2 matches.
master.guess("abcczz") returns 4, because "abcczz" has 4 matches.
We made 5 calls to master.guess, and one of them was the secret, so we pass the test case.

Example 2:

Input: secret = "hamada", words = ["hamada","khaled"], allowedGuesses = 10
Output: You guessed the secret word correctly.
Explanation: Since there are two words, you can guess both.

Constraints:

	1 <= words.length <= 100
	words[i].length == 6
	words[i] consist of lowercase English letters.
	All the strings of wordlist are unique.
	secret exists in words.
	10 <= allowedGuesses <= 30
"""
import random
from typing import List
import pytest
import sys


# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
class Master:
    def __init__(self, secret, words, allowedGuesses):
        self.secret = secret
        self.words = words
        self.allowedGuesses = allowedGuesses

    def guess(self, word: str) -> int:
        if self.allowedGuesses == 0:
            raise Exception(f'allowedGuesses exceeded')
        self.allowedGuesses -= 1
        if word not in self.words:
            return -1
        return len([1 for a, b in zip(self.secret, word) if a == b])


class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        """Apr 17, 2024 19:12"""
        FALSE = "Either you took too many guesses, or you did not find the secret word."
        TRUE = "You guessed the secret word correctly."

        def count_matches(s1, s2):
            return len([1 for a, b in zip(s1, s2) if a == b])

        random.shuffle(words)
        pivot = -1
        while words:
            matches = master.guess(words[-1])
            _words = []
            if matches == 6:
                return TRUE
            else:
                for i in range(len(words)-1):
                    if count_matches(words[-1], words[i]) == matches:
                        _words.append(words[i])
            words = _words

        return FALSE



@pytest.mark.parametrize('args', [
    (("acckzz", ["acckzz","ccbazz","eiowzz","abcczz"], 10, 'You guessed the secret word correctly.')),
    (("hamada", ["hamada","khaled"], 10, 'You guessed the secret word correctly.')),
    # (('hbaczn', ["gaxckt","trlccr","jxwhkz","ycbfps","peayuf","yiejjw","ldzccp","nqsjoa","qrjasy","pcldos","acrtag","buyeia","ubmtpj","drtclz","zqderp","snywek","caoztp","ibpghw","evtkhl","bhpfla","ymqhxk","qkvipb","tvmued","rvbass","axeasm","qolsjg","roswcb","vdjgxx","bugbyv","zipjpc","tamszl","osdifo","dvxlxm","iwmyfb","wmnwhe","hslnop","nkrfwn","puvgve","rqsqpq","jwoswl","tittgf","evqsqe","aishiv","pmwovj","sorbte","hbaczn","coifed","hrctvp","vkytbw","dizcxz","arabol","uywurk","ppywdo","resfls","tmoliy","etriev","oanvlx","wcsnzy","loufkw","onnwcy","novblw","mtxgwe","rgrdbt","ckolob","kxnflb","phonmg","egcdab","cykndr","lkzobv","ifwmwp","jqmbib","mypnvf","lnrgnj","clijwa","kiioqr","syzebr","rqsmhg","sczjmz","hsdjfp","mjcgvm","ajotcx","olgnfv","mjyjxj","wzgbmg","lpcnbj","yjjlwn","blrogv","bdplzs","oxblph","twejel","rupapy","euwrrz","apiqzu","ydcroj","ldvzgq","zailgu","xgqpsr","wxdyho","alrplq","brklfk"], 10, '')),
])
def test(args):
    secret, words, allowedGuesses, expected = args
    assert expected == Solution().findSecretWord(words, Master(secret, words, allowedGuesses))


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
