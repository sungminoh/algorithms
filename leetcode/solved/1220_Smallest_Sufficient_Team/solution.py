#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 sungminoh <smoh2044@gmail.com>
#
# Distributed under terms of the MIT license.

"""
In a project, you have a list of required skills req_skills, and a list of people. The ith person people[i] contains a list of skills that the person has.

Consider a sufficient team: a set of people such that for every required skill in req_skills, there is at least one person in the team who has that skill. We can represent these teams by the index of each person.

	For example, team = [0, 1, 3] represents the people with skills people[0], people[1], and people[3].

Return any sufficient team of the smallest possible size, represented by the index of each person. You may return the answer in any order.

It is guaranteed an answer exists.

Example 1:
Input: req_skills = ["java","nodejs","reactjs"], people = [["java"],["nodejs"],["nodejs","reactjs"]]
Output: [0,2]
Example 2:
Input: req_skills = ["algorithms","math","java","reactjs","csharp","aws"], people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
Output: [1,2]

Constraints:

	1 <= req_skills.length <= 16
	1 <= req_skills[i].length <= 16
	req_skills[i] consists of lowercase English letters.
	All the strings of req_skills are unique.
	1 <= people.length <= 60
	0 <= people[i].length <= 16
	1 <= people[i][j].length <= 16
	people[i][j] consists of lowercase English letters.
	All the strings of people[i] are unique.
	Every skill in people[i] is a skill in req_skills.
	It is guaranteed a sufficient team exists.
"""
from typing import List
import pytest
import sys


class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        """TLE May 04, 2024 16:27"""
        skill_id = {s: i for i, s in enumerate(req_skills)}
        def encode(person):
            ret = 0
            for s in person:
                ret |= 1<<skill_id[s]
            return ret

        skills = [encode(p) for p in people]

        ret = list(range(len(people)))
        ALL = (1<<len(skill_id)) - 1
        def dfs(i, has, acc):
            nonlocal ret
            if len(acc) > len(ret):
                return
            if has == ALL:
                ret = acc[:]
                return
            if i == len(people):
                return
            acc.append(i)
            dfs(i+1, has | skills[i], acc)
            acc.pop()
            dfs(i+1, has, acc)

        dfs(0, 0, [])

        return ret

    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        """May 04, 2024 16:37"""
        skill_id = {s: i for i, s in enumerate(req_skills)}
        skill_owners = [[] for _ in range(len(skill_id))]
        for i, p in enumerate(people):
            for s in p:
                skill_owners[skill_id[s]].append(i)

        def encode(person):
            ret = 0
            for s in person:
                ret |= 1<<skill_id[s]
            return ret

        skills = [encode(p) for p in people]

        ret = list(range(len(skill_id)))
        def dfs(i, acc, cur):
            nonlocal ret
            if len(acc) > len(ret):
                return
            if i == len(skill_id):
                ret = list(acc)
                return
            if (1<<i) & cur:
                dfs(i+1, acc, cur)
            else:
                for j in skill_owners[i]:
                    if j not in acc:
                        acc.add(j)
                        dfs(i+1, acc, cur | skills[j])
                        acc.discard(j)

        dfs(0, set(), 0)
        return ret


@pytest.mark.parametrize('args', [
    ((["java","nodejs","reactjs"], [["java"],["nodejs"],["nodejs","reactjs"]], [0,2])),
    ((["algorithms","math","java","reactjs","csharp","aws"], [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]], [1,2])),
    ((["gzkytqcynt","kcoobskzamd","ddofnsczakzrocob","zjqdvz","mksriiu","aeuauwedm","u","y"], [["ddofnsczakzrocob","zjqdvz","mksriiu"],["zjqdvz"],[],["kcoobskzamd","ddofnsczakzrocob","mksriiu"],["mksriiu"],["y"],["kcoobskzamd","zjqdvz"],[],["zjqdvz","mksriiu"],["gzkytqcynt","u"],[],[],["u"],[],["mksriiu"],["ddofnsczakzrocob","mksriiu","aeuauwedm"],["gzkytqcynt","zjqdvz","y"],[],["zjqdvz"],[],["mksriiu","u"],[],[],[],["gzkytqcynt"],["ddofnsczakzrocob","zjqdvz"],["gzkytqcynt","ddofnsczakzrocob"],[],[],["zjqdvz","u"],["mksriiu","aeuauwedm"],["zjqdvz"],[],[],["gzkytqcynt","ddofnsczakzrocob","zjqdvz","mksriiu"],["gzkytqcynt","ddofnsczakzrocob","zjqdvz","mksriiu"],["ddofnsczakzrocob","zjqdvz"],["u"],["gzkytqcynt"],["ddofnsczakzrocob","mksriiu","u"],["y"],["mksriiu"],["ddofnsczakzrocob","zjqdvz","y"],["ddofnsczakzrocob"],["mksriiu"],["u"],["mksriiu"],["mksriiu"],["ddofnsczakzrocob"],["ddofnsczakzrocob","mksriiu","y"]], [6, 16, 30, 39])),
])
def test(args):
    actual = Solution().smallestSufficientTeam(*args[:-1])
    assert set(args[-1]) == set(actual)



if __name__ == '__main__':
    sys.exit(pytest.main(["-s", "-v"] + sys.argv))
