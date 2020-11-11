### [640. Solve the Equation](https://leetcode.com/problems/solve-the-equation/)

Medium

Solve a given equation and return the value of `` x `` in the form of string "x=\#value". The equation contains only '+', '-' operation, the variable `` x `` and its coefficient.

If there is no solution for the equation, return "No solution".

If there are infinite solutions for the equation, return "Infinite solutions".

If there is exactly one solution for the equation, we ensure that the value of `` x `` is an integer.

__Example 1:__  

```
<b>Input:</b> "x+5-3+x=6+x-2"
<b>Output:</b> "x=2"
```

__Example 2:__  

```
<b>Input:</b> "x=x"
<b>Output:</b> "Infinite solutions"
```

__Example 3:__  

```
<b>Input:</b> "2x=x"
<b>Output:</b> "x=0"
```

__Example 4:__  

```
<b>Input:</b> "2x+3x-6x=x+2"
<b>Output:</b> "x=-1"
```

__Example 5:__  

```
<b>Input:</b> "x=x+2"
<b>Output:</b> "No solution"
```

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 57,917 | 24,180 | 41.7% |