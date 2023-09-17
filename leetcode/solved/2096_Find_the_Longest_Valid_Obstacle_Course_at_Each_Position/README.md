### [2096. Find the Longest Valid Obstacle Course at Each Position](https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/?envType=daily-question&envId=2023-05-07)

Hard

You want to build some obstacle courses. You are given a __0-indexed__ integer array `` obstacles `` of length `` n ``, where `` obstacles[i] `` describes the height of the <code>i<sup>th</sup></code> obstacle.

For every index `` i `` between `` 0 `` and `` n - 1 `` (__inclusive__), find the length of the __longest obstacle course__ in `` obstacles `` such that:

*   You choose any number of obstacles between `` 0 `` and `` i `` __inclusive__.
*   You must include the <code>i<sup>th</sup></code> obstacle in the course.
*   You must put the chosen obstacles in the __same order__ as they appear in `` obstacles ``.
*   Every obstacle (except the first) is __taller__ than or the __same height__ as the obstacle immediately before it.

Return _an array_ `` ans `` _of length_ `` n ``, _where_ `` ans[i] `` _is the length of the __longest obstacle course__ for index_ `` i ``_ as described above_.

 

<strong class="example">Example 1:</strong>

```
Input: obstacles = [1,2,3,2]
Output: [1,2,3,3]
Explanation: The longest valid obstacle course at each position is:
- i = 0: [<u>1</u>], [1] has length 1.
- i = 1: [<u>1</u>,<u>2</u>], [1,2] has length 2.
- i = 2: [<u>1</u>,<u>2</u>,<u>3</u>], [1,2,3] has length 3.
- i = 3: [<u>1</u>,<u>2</u>,3,<u>2</u>], [1,2,2] has length 3.
```

<strong class="example">Example 2:</strong>

```
Input: obstacles = [2,2,1]
Output: [1,2,1]
Explanation: The longest valid obstacle course at each position is:
- i = 0: [<u>2</u>], [2] has length 1.
- i = 1: [<u>2</u>,<u>2</u>], [2,2] has length 2.
- i = 2: [2,2,<u>1</u>], [1] has length 1.
```

<strong class="example">Example 3:</strong>

```
Input: obstacles = [3,1,5,6,4,2]
Output: [1,1,2,3,2,2]
Explanation: The longest valid obstacle course at each position is:
- i = 0: [<u>3</u>], [3] has length 1.
- i = 1: [3,<u>1</u>], [1] has length 1.
- i = 2: [<u>3</u>,1,<u>5</u>], [3,5] has length 2. [1,5] is also valid.
- i = 3: [<u>3</u>,1,<u>5</u>,<u>6</u>], [3,5,6] has length 3. [1,5,6] is also valid.
- i = 4: [<u>3</u>,1,5,6,<u>4</u>], [3,4] has length 2. [1,4] is also valid.
- i = 5: [3,<u>1</u>,5,6,4,<u>2</u>], [1,2] has length 2.
```

 

__Constraints:__

*   `` n == obstacles.length ``
*   <code>1 <= n <= 10<sup>5</sup></code>
*   <code>1 <= obstacles[i] <= 10<sup>7</sup></code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 82,813 | 52,700 | 63.6% |