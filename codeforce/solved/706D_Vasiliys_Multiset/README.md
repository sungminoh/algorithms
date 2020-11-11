### [D. Vasiliy's Multiset](http://codeforces.com/problemset/problem/706/D)

- time limit per test: 4 seconds
- memory limit per test: 256 megabytes
- input: standard input
- output: standard output

Author has gone out of the stories about Vasiliy, so here is just a formal task description.

You are given *q* queries and a multiset *A*, initially containing only integer 0. There are three types of queries:

1. "+ x" — add integer *x* to multiset *A*.
2. "- x" — erase one occurrence of integer *x* from multiset *A*. It's guaranteed that at least one *x* is present in the multiset *A* before this query.
3. "? x" — you are given integer *x* and need to compute the value ![img](http://codeforces.com/predownloaded/af/1b/af1b4d5401ef843e35de22bbd1367fa78816de31.png), i.e. the maximum value of bitwise exclusive OR (also know as XOR) of integer *x* and some integer *y* from the multiset *A*.

Multiset is a set, where equal elements are allowed.

#### Input

The first line of the input contains a single integer *q* (1 ≤ *q* ≤ 200 000) — the number of queries Vasiliy has to perform.

Each of the following *q* lines of the input contains one of three characters '+', '-' or '?' and an integer *x**i* (1 ≤ *x**i* ≤ 109). It's guaranteed that there is at least one query of the third type.

Note, that the integer 0 will always be present in the set *A*.

#### Output

For each query of the type '?' print one integer — the maximum value of bitwise exclusive OR (XOR) of integer *x**i* and some integer from the multiset *A*.

#### Example

input

```
10
+ 8
+ 9
+ 11
+ 6
+ 1
? 3
- 8
? 3
? 8
? 11

```

output

```
11
10
14
13

```

#### Note

After first five operations multiset *A* contains integers 0, 8, 9, 11, 6 and 1.

The answer for the sixth query is integer ![img](http://codeforces.com/predownloaded/f1/be/f1be3f0eb002b70f2885010a36a4ee3437035f76.png) — maximum among integers ![img](http://codeforces.com/predownloaded/37/b9/37b978f8f58974079cd14c236f215799c4498de1.png), ![img](http://codeforces.com/predownloaded/5d/c1/5dc10ff70d05fbc23f9ca460fcdaabd323da2000.png), ![img](http://codeforces.com/predownloaded/25/ea/25eadc76e65c2dcc9e605d7cbcb8b85c432154b6.png), ![img](http://codeforces.com/predownloaded/4e/9f/4e9f7b2b7c9c3c4a682f5417c5422483016ee463.png) and ![img](http://codeforces.com/predownloaded/6f/0d/6f0d4181cb4df733db930b2d79c66c1f83fafd42.png).