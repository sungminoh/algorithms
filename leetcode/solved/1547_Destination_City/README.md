### [1547. Destination City](https://leetcode.com/problems/destination-city/description/?envType=daily-question&envId=2023-12-15)

Easy

You are given the array `` paths ``, where <code>paths[i] = [cityA<sub>i</sub>, cityB<sub>i</sub>]</code> means there exists a direct path going from <code>cityA<sub>i</sub></code> to <code>cityB<sub>i</sub></code>. _Return the destination city, that is, the city without any path outgoing to another city._

It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

 

<strong class="example">Example 1:</strong>

```
Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo" 
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".
```

<strong class="example">Example 2:</strong>

```
Input: paths = [["B","C"],["D","B"],["C","A"]]
Output: "A"
Explanation: All possible trips are: 
"D" -> "B" -> "C" -> "A". 
"B" -> "C" -> "A". 
"C" -> "A". 
"A". 
Clearly the destination city is "A".
```

<strong class="example">Example 3:</strong>

```
Input: paths = [["A","Z"]]
Output: "Z"
```

 

__Constraints:__

*   `` 1 <= paths.length <= 100 ``
*   `` paths[i].length == 2 ``
*   <code>1 <= cityA<sub>i</sub>.length, cityB<sub>i</sub>.length <= 10</code>
*   <code>cityA<sub>i</sub> != cityB<sub>i</sub></code>
*   All strings consist of lowercase and uppercase English letters and the space character.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 309,295 | 246,853 | 79.8% |