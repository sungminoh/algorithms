### [282. Expression Add Operators](https://leetcode.com/problems/expression-add-operators/)

Hard

Given a string `` num `` that contains only digits and an integer `` target ``, return ___all possibilities__ to insert the binary operators _`` '+' ``_, _`` '-' ``_, and/or _`` '*' ``_ between the digits of _`` num ``_ so that the resultant expression evaluates to the _`` target ``_ value_.

Note that operands in the returned expressions __should not__ contain leading zeros.

 

__Example 1:__

```
Input: num = "123", target = 6
Output: ["1*2*3","1+2+3"]
Explanation: Both "1*2*3" and "1+2+3" evaluate to 6.
```

__Example 2:__

```
Input: num = "232", target = 8
Output: ["2*3+2","2+3*2"]
Explanation: Both "2*3+2" and "2+3*2" evaluate to 8.
```

__Example 3:__

```
Input: num = "105", target = 5
Output: ["1*0+5","10-5"]
Explanation: Both "1*0+5" and "10-5" evaluate to 5.
Note that "1-05" is not a valid expression because the 5 has a leading zero.
```

__Example 4:__

```
Input: num = "00", target = 0
Output: ["0*0","0+0","0-0"]
Explanation: "0*0", "0+0", and "0-0" all evaluate to 0.
Note that "00" is not a valid expression because the 0 has a leading zero.
```

__Example 5:__

```
Input: num = "3456237490", target = 9191
Output: []
Explanation: There are no expressions that can be created from "3456237490" to evaluate to 9191.
```

 

__Constraints:__

*   `` 1 <= num.length <= 10 ``
*   `` num `` consists of only digits.
*   <code>-2<sup>31</sup> <= target <= 2<sup>31</sup> - 1</code>

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 405,595 | 156,503 | 38.6% |