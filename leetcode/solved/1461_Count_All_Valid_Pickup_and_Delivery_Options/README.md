### [1461. Count All Valid Pickup and Delivery Options](https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/)

Hard

Given `` n `` orders, each order consist in pickup and delivery services. 

Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i). 

Since the answer may be too large, return it modulo 10^9 + 7.

 

__Example 1:__

```
Input: n = 1
Output: 1
Explanation: Unique order (P1, D1), Delivery 1 always is after of Pickup 1.
```

__Example 2:__

```
Input: n = 2
Output: 6
Explanation: All possible orders: 
(P1,P2,D1,D2), (P1,P2,D2,D1), (P1,D1,P2,D2), (P2,P1,D1,D2), (P2,P1,D2,D1) and (P2,D2,P1,D1).
This is an invalid order (P1,D2,P2,D1) because Pickup 2 is after of Delivery 2.
```

__Example 3:__

```
Input: n = 3
Output: 90
```

 

__Constraints:__

*   `` 1 <= n <= 500 ``

| Submissions    | Accepted     | Rate   |
| -------------- | ------------ | ------ |
| 79,486 | 50,349 | 63.3% |