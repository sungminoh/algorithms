#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example 1:

Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.

Example 2:

Input: s = "a"
Output: 0

Example 3:

Input: s = "ab"
Output: 1

Constraints:

	1 <= s.length <= 2000
	s consists of lower-case English letters only.
"""
from functools import lru_cache
import sys
import pytest


@lru_cache(None)
def is_palindrome(s):
    return s[:len(s)//2] == s[(len(s)+1)//2:][::-1]


class Solution:
    def minCut(self, s):
        """08/18/2018 05:45"""
        @lru_cache(None)
        def n_cut(i):
            if is_palindrome(s[i:]):
                return 0
            for j in range(1, len(s)):
                if is_palindrome(s[:j]) and is_palindrome(s[j:]):
                    return 1
            m = float('inf')
            for j in range(len(s)-1, i, -1):
                if is_palindrome(s[i:j]):
                    m = min(m, 1 + n_cut(j))
            return m
        return n_cut(0)

    def minCut(self, s: str) -> int:
        """04/11/2020 23:24"""
        palindrome = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            palindrome[i][i] = True
        for i in range(len(s) - 1):
            palindrome[i][i + 1] = s[i] == s[i + 1]
        for k in range(2, len(s)):
            for i in range(len(s) - k):
                palindrome[i][i+k] = palindrome[i+1][i+k-1] and s[i] == s[i+k]

        cut = [float('inf')] * len(s)
        cut[0] = 0
        for j in range(len(cut)):
            if palindrome[0][j]:
                cut[j] = 0
            else:
                for i in range(0, j):
                    if palindrome[j-i][j]:
                        cut[j] = min(cut[j], cut[j-i-1] + 1)
        return cut[-1]

    def minCut(self, s: str) -> int:
        """
        Time complexity: O(n^2)
        Space complexity: O(n^2)
        """
        @lru_cache(None)
        def is_palindrome(i, j):
            if i >= j:
                return True
            return s[i] == s[j] and is_palindrome(i+1, j-1)

        if is_palindrome(0, len(s)-1):
            return 0
        dp = [len(s)-1] * len(s)
        dp[0] = 0
        for i in range(1, len(dp)):
            if is_palindrome(0, i):
                dp[i] = 0
            else:
                for j in range(1, i+1):
                    if is_palindrome(j, i):
                        dp[i] = min(dp[i], dp[j-1] + 1)
        return dp[-1]


@pytest.mark.parametrize('s, expected', [
    ("aab", 1),
    ("a", 0),
    ("ab", 1),
    ("bb", 0),
    ("cdd", 1),
    ("abcccb", 1),
    ("abcde", 4),
    ("abcdefghijklmnopqrstuvwxyz", 25),
    ("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz", 51),
    ("eegiicgaeadbcfacfhifdbiehbgejcaeggcgbahfcajfhjjdgj", 42),
    ("efe", 0),
    ("apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp", 452),
    ("adabdcaebdcebdcacaaaadbbcadabcbeabaadcbcaaddebdbddcbdacdbbaedbdaaecabdceddccbdeeddccdaabbabbdedaaabcdadbdabeacbeadbaddcbaacdbabcccbaceedbcccedbeecbccaecadccbdbdccbcbaacccbddcccbaedbacdbcaccdcaadcbaebebcceabbdcdeaabdbabadeaaaaedbdbcebcbddebccacacddebecabccbbdcbecbaeedcdacdcbdbebbacddddaabaedabbaaabaddcdaadcccdeebcabacdadbaacdccbeceddeebbbdbaaaaabaeecccaebdeabddacbedededebdebabdbcbdcbadbeeceecdcdbbdcbdbeeebcdcabdeeacabdeaedebbcaacdadaecbccbededceceabdcabdeabbcdecdedadcaebaababeedcaacdbdacbccdbcece", 273),
    ("fiefhgdcdcgfeibggchibffahiededbbegegdfibdbfdadfbdbceaadeceeefiheibahgececggaehbdcgebaigfacifhdbecbebfhiefchaaheiichgdbheacfbhfiaffaecicbegdgeiaiccghggdfggbebdaefcagihbdhhigdgbghbahhhdagbdaefeccfiaifffcfehfcdiiieibadcedibbedgfegibefagfccahfcbegdfdhhdgfhgbchiaieehdgdabhidhfeecgfiibediiafacagigbhchcdhbaigdcedggehhgdhedaebchcafcdehcffdiagcafcgiidhdhedgaaegdchibhdaegdfdaiiidcihifbfidechicighbcbgibadbabieaafgeagfhebfaheaeeibagdfhadifafghbfihehgcgggffgbfccgafigieadfehieafaehaggeeaaaehggffccddchibegfhdfafhadgeieggiigacbfgcagigbhbhefcadafhafdiegahbhccidbeeagcgebehheebfaechceefdiafgeddhdfcadfdafbhiifigcbddahbabbeedidhaieagheihhgffbfbiacgdaifbedaegbhigghfeiahcdieghhdabdggfcgbafgibiifdeefcbegcfcdihaeacihgdchihdadifeifdgecbchgdgdcifedacfddhhbcagaicbebbiadgbddcbagbafeadhddaeebdgdebafabghcabdhdgieiahggddigefddccfccibifgbfcdccghgceigdfdbghdihechfabhbacifgbiiiihcgifhdbhfcaiefhccibebcahidachfabicbdabibiachahggffiibbgchbidfbbhfcicfafgcagaaadbacddfiigdiiffhbbehaaacidggfbhgeaghigihggfcdcidbfccahhgaffiibbhidhdacacdfebedbiacaidaachegffaiiegeabfdgdcgdacfcfhdcbfiaaifgfaciacfghagceaaebhhibbieehhcbiggabefbeigcbhbcidbfhfcgdddgdffghidbbbfbdhcgabaagddcebaechbbiegeiggbabdhgghciheabdibefdfghbfbfebidhicdhbeghebeddgfdfhefebiiebdchifbcbahaddhbfafbbcebiigadhgcfbebgbebhfddgdeehhgdegaeedfadegfeihcgeefbbagbbacbgggciehdhiggcgaaicceeaefgcehfhfdciaghcbbgdihbhecfbgffefhgiefgeiggcebgaacefidghdfdhiabgibchdicdehahbibeddegfciaeaffgbefbbeihbafbagagedgbdadfdggfeaebaidchgdbcifhahgfdcehbahhdggcdggceiabhhafghegfdiegbcadgaecdcdddfhicabdfhbdiiceiegiedecdifhbhhfhgdbhibbdgafhgdcheefdhifgddchadbdggiidhbhegbdfdidhhfbehibiaacdfbiagcbheabaaebfeaeafbgigiefeaeheabifgcfibiddadicheahgbfhbhddaheghddceedigddhchecaghdegigbegcbfgbggdgbbigegffhcfcbbebdchffhddbfhhfgegggibhafiebcfgeaeehgdgbccbfghagfdbdfcbcigbigaccecfehcffahiafgabfcaefbghccieehhhiighcfeabffggfchfdgcfhadgidabdceediefdccceidcfbfiiaidechhbhdccccaigeegcaicabbifigcghcefaafaefd", 1345),
])
def test(s, expected):
    assert expected == Solution().minCut(s)


if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
