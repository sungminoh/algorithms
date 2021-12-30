### [210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)

Medium

There are a total of `` numCourses `` courses you have to take, labeled from `` 0 `` to `` numCourses - 1 ``. You are given an array `` prerequisites `` where <code>prerequisites[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> indicates that you __must__ take course <code>b<sub>i</sub></code> first if you want to take course <code>a<sub>i</sub></code>.

*   For example, the pair `` [0, 1] ``, indicates that to take course `` 0 `` you have to first take course `` 1 ``.

Return _the ordering of courses you should take to finish all courses_. If there are many valid answers, return __any__ of them. If it is impossible to finish all courses, return __an empty array__.

 

__Example 1:__

```
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
```

__Example 2:__

```
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
```

__Example 3:__

```
Input: numCourses = 1, prerequisites = []
Output: [0]
```

 

__Constraints:__

*   `` 1 <= numCourses <= 2000 ``
*   `` 0 <= prerequisites.length <= numCourses * (numCourses - 1) ``
*   `` prerequisites[i].length == 2 ``
*   <code>0 <= a<sub>i</sub>, b<sub>i</sub> < numCourses</code>
*   <code>a<sub>i</sub> != b<sub>i</sub></code>
*   All the pairs <code>[a<sub>i</sub>, b<sub>i</sub>]</code> are __distinct__.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 1,184,245 | 539,887 | 45.6% |