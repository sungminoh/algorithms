### [282. Expression Add Operators](https://leetcode.com/problems/expression-add-operators/)

Hard

Given a string that contains only digits `` 0-9 `` and a target value, return all possibilities to add __binary__ operators (not unary) `` + ``, `` - ``, or `` * `` between the digits so they evaluate to the target value.

__Example 1:__

```
<b>Input:</b> <code><em>num</em> = </code>"123", <em>target</em> = 6
<b>Output: </b>["1+2+3", "1*2*3"] 
```

__Example 2:__

```
<b>Input:</b> <code><em>num</em> = </code>"232", <em>target</em> = 8
<b>Output: </b>["2*3+2", "2+3*2"]
```

__Example 3:__

```
<b>Input:</b> <code><em>num</em> = </code>"105", <em>target</em> = 5
<b>Output: </b>["1*0+5","10-5"]
```

__Example 4:__

```
<b>Input:</b> <code><em>num</em> = </code>"00", <em>target</em> = 0
<b>Output: </b>["0+0", "0-0", "0*0"]
```

__Example 5:__

```
<b>Input:</b> <code><em>num</em> = </code>"3456237490", <em>target</em> = 9191
<b>Output: </b>[]
```

 

__Constraints:__

*   `` 0 <= num.length <= 10 ``
*   `` num `` only contain digits.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 282,879 | 99,836 | 35.3% |