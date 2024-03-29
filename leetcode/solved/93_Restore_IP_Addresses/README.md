### [93. Restore IP Addresses](https://leetcode.com/problems/restore-ip-addresses/)

Medium

A __valid IP address__ consists of exactly four integers separated by single dots. Each integer is between `` 0 `` and `` 255 `` (__inclusive__) and cannot have leading zeros.

*   For example, `` "0.1.2.201" `` and `` "192.168.1.1" `` are __valid__ IP addresses, but `` "0.011.255.245" ``, `` "192.168.1.312" `` and `` "192.168@1.1" `` are __invalid__ IP addresses.

Given a string `` s `` containing only digits, return _all possible valid IP addresses that can be formed by inserting dots into _`` s ``. You are __not__ allowed to reorder or remove any digits in `` s ``. You may return the valid IP addresses in __any__ order.

 

<strong class="example">Example 1:</strong>

```
Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]
```

<strong class="example">Example 2:</strong>

```
Input: s = "0000"
Output: ["0.0.0.0"]
```

<strong class="example">Example 3:</strong>

```
Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
```

 

__Constraints:__

*   `` 1 <= s.length <= 20 ``
*   `` s `` consists of digits only.

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 832,945 | 393,546 | 47.2% |