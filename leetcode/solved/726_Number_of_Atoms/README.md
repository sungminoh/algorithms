### [726. Number of Atoms](https://leetcode.com/problems/number-of-atoms/description/?envType=daily-question&envId=2024-07-14)

Hard

Given a string `` formula `` representing a chemical formula, return _the count of each atom_.

The atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.

One or more digits representing that element's count may follow if the count is greater than `` 1 ``. If the count is `` 1 ``, no digits will follow.

*   For example, `` "H2O" `` and `` "H2O2" `` are possible, but `` "H1O2" `` is impossible.

Two formulas are concatenated together to produce another formula.

*   For example, `` "H2O2He3Mg4" `` is also a formula.

A formula placed in parentheses, and a count (optionally added) is also a formula.

*   For example, `` "(H2O2)" `` and `` "(H2O2)3" `` are formulas.

Return the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than `` 1 ``), followed by the second name (in sorted order), followed by its count (if that count is more than `` 1 ``), and so on.

The test cases are generated so that all the values in the output fit in a __32-bit__ integer.

 

<strong class="example">Example 1:</strong>

```
Input: formula = "H2O"
Output: "H2O"
Explanation: The count of elements are {'H': 2, 'O': 1}.
```

<strong class="example">Example 2:</strong>

```
Input: formula = "Mg(OH)2"
Output: "H2MgO2"
Explanation: The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.
```

<strong class="example">Example 3:</strong>

```
Input: formula = "K4(ON(SO3)2)2"
Output: "K4N2O14S4"
Explanation: The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.
```

 

__Constraints:__

*   `` 1 <= formula.length <= 1000 ``
*   `` formula `` consists of English letters, digits, `` '(' ``, and `` ')' ``.
*   `` formula `` is always valid.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 225,013 | 146,669 | 65.2% |