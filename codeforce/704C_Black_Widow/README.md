### [C. Black Widow](http://codeforces.com/problemset/problem/704/C)

- time limit per test: 2 seconds
- memory limit per test: 256 megabytes
- input: standard input
- output: standard output

Natalia Romanova is trying to test something on the new gun S.H.I.E.L.D gave her. In order to determine the result of the test, she needs to find the number of answers to a certain equation. The equation is of form:

![img](http://codeforces.com/predownloaded/0d/63/0d637ea7cd9d50e60ff47db836c3a91e0eb849b0.png)

Where ![img](http://codeforces.com/predownloaded/f6/6d/f66d5a8baeb3645356745f84de710ee8bca95c8d.png) represents logical OR and ![img](http://codeforces.com/predownloaded/7b/ea/7beade55e90846d70020a3d03521d3458b66751b.png) represents logical exclusive OR (XOR), and *v**i*, *j* are some boolean variables or their negations. Natalia calls the left side of the equation a XNF formula. Each statement in brackets is called a clause, and *v**i*, *j* are called literals.

In the equation Natalia has, the left side is actually a 2-XNF-2 containing variables *x*1, *x*2, ..., *x**m* and their negations. An XNF formula is 2-XNF-2 if:

1. For each 1 ≤ *i* ≤ *n*, *k**i* ≤ 2, i.e. the size of each clause doesn't exceed two.
2. Each variable occurs **in the formula at most two times** (with negation and without negation in total). Please note that it's possible that a variable occurs twice but its negation doesn't occur in any clause (or vice versa).

Natalia is given a formula of *m* variables, consisting of *n* clauses. Please, make sure to check the samples in order to properly understand how the formula looks like.

Natalia is more into fight than theory, so she asked you to tell her the number of answers to this equation. More precisely, you need to find the number of ways to set *x*1, ..., *x**m* with *true* and *false* (out of total of 2*m* ways) so that the equation is satisfied. Since this number can be extremely large, you need to print the answer modulo 109 + 7.

Please, note that some variable may appear twice in one clause, or not appear in the equation at all (but still, setting it to *false* or *true*gives different ways to set variables).

#### Input

The first line of input contains two integers *n* and *m* (1 ≤ *n*, *m* ≤ 100 000) — the number of clauses and the number of variables respectively.

The next *n* lines contain the formula. The *i*-th of them starts with an integer *k**i* — the number of literals in the *i*-th clause. It is followed by *k**i* non-zero integers *a**i*, 1, ..., *a**i*, *k**i*. If *a**i*, *j* > 0 then *v**i*, *j* is *x**a**i*, *j* otherwise it's negation of *x* - *a**i*, *j* (1 ≤ *k**i* ≤ 2,  - *m* ≤ *a**i*, *j* ≤ *m*, *a**i*, *j* ≠ 0).

#### Output

Print the answer modulo 1 000 000 007 (109 + 7) in one line.

#### Examples

input

```
6 7
2 4 -2
2 6 3
2 -7 1
2 -5 1
2 3 6
2 -2 -5

```

output

```
48

```

input

```
8 10
1 -5
2 4 -6
2 -2 -6
2 -7 9
2 10 -1
2 3 -1
2 -8 9
2 5 8

```

output

```
544

```

input

```
2 3
2 1 1
2 -3 3

```

output

```
4

```

#### Note

The equation in the first sample is:

![img](http://codeforces.com/predownloaded/28/8f/288f07e976c1475cdda679f67942ae7779907997.png)

The equation in the second sample is:

![img](http://codeforces.com/predownloaded/16/97/1697cc609520b34073afa6e868af4687f02d96a5.png)

The equation in the third sample is:

![img](http://codeforces.com/predownloaded/14/91/149195216145c6b69c5cf61dd873530f481f8a68.png)