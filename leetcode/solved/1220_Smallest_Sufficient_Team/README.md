### [1220. Smallest Sufficient Team](https://leetcode.com/problems/smallest-sufficient-team/description/)

Hard

In a project, you have a list of required skills `` req_skills ``, and a list of people. The <code>i<sup>th</sup></code> person `` people[i] `` contains a list of skills that the person has.

Consider a sufficient team: a set of people such that for every required skill in `` req_skills ``, there is at least one person in the team who has that skill. We can represent these teams by the index of each person.

*   For example, `` team = [0, 1, 3] `` represents the people with skills `` people[0] ``, `` people[1] ``, and `` people[3] ``.

Return _any sufficient team of the smallest possible size, represented by the index of each person_. You may return the answer in __any order__.

It is __guaranteed__ an answer exists.

 

<strong class="example">Example 1:</strong>

```Input: req_skills = ["java","nodejs","reactjs"], people = [["java"],["nodejs"],["nodejs","reactjs"]]
Output: [0,2]
```

<strong class="example">Example 2:</strong>

```Input: req_skills = ["algorithms","math","java","reactjs","csharp","aws"], people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
Output: [1,2]
```

 

__Constraints:__

*   `` 1 <= req_skills.length <= 16 ``
*   `` 1 <= req_skills[i].length <= 16 ``
*   `` req_skills[i] `` consists of lowercase English letters.
*   All the strings of `` req_skills `` are __unique__.
*   `` 1 <= people.length <= 60 ``
*   `` 0 <= people[i].length <= 16 ``
*   `` 1 <= people[i][j].length <= 16 ``
*   `` people[i][j] `` consists of lowercase English letters.
*   All the strings of `` people[i] `` are __unique__.
*   Every skill in `` people[i] `` is a skill in `` req_skills ``.
*   It is guaranteed a sufficient team exists.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 110,964 | 61,898 | 55.8% |