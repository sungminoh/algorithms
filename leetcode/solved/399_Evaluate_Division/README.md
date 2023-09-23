### [399. Evaluate Division](https://leetcode.com/problems/evaluate-division/?envType=daily-question&envId=2023-05-20)

Medium

You are given an array of variable pairs `` equations `` and an array of real numbers `` values ``, where <code>equations[i] = [A<sub>i</sub>, B<sub>i</sub>]</code> and `` values[i] `` represent the equation <code>A<sub>i</sub> / B<sub>i</sub> = values[i]</code>. Each <code>A<sub>i</sub></code> or <code>B<sub>i</sub></code> is a string that represents a single variable.

You are also given some `` queries ``, where <code>queries[j] = [C<sub>j</sub>, D<sub>j</sub>]</code> represents the <code>j<sup>th</sup></code> query where you must find the answer for <code>C<sub>j</sub> / D<sub>j</sub> = ?</code>.

Return _the answers to all queries_. If a single answer cannot be determined, return `` -1.0 ``.

__Note:__ The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

__Note: __The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

 

<strong class="example">Example 1:</strong>

```
Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: <em>a / b = 2.0</em>, <em>b / c = 3.0</em>
queries are: <em>a / c = ?</em>, <em>b / a = ?</em>, <em>a / e = ?</em>, <em>a / a = ?</em>, <em>x / x = ? </em>
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined => -1.0
```

<strong class="example">Example 2:</strong>

```
Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]
```

<strong class="example">Example 3:</strong>

```
Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]
```

 

__Constraints:__

*   `` 1 <= equations.length <= 20 ``
*   `` equations[i].length == 2 ``
*   <code>1 <= A<sub>i</sub>.length, B<sub>i</sub>.length <= 5</code>
*   `` values.length == equations.length ``
*   `` 0.0 < values[i] <= 20.0 ``
*   `` 1 <= queries.length <= 20 ``
*   `` queries[i].length == 2 ``
*   <code>1 <= C<sub>j</sub>.length, D<sub>j</sub>.length <= 5</code>
*   <code>A<sub>i</sub>, B<sub>i</sub>, C<sub>j</sub>, D<sub>j</sub></code> consist of lower case English letters and digits.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 658,907 | 404,486 | 61.4% |