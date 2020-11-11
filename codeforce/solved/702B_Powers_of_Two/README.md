### [B. Powers of Two](http://codeforces.com/problemset/problem/702/B)

- time limit per test: 3 seconds
- memory limit per test: 256 megabytes
- input: standard input
- output: standard output

You are given *n* integers *a*1, *a*2, ..., *a**n*. Find the number of pairs of indexes *i*, *j* (*i* < *j*) that *a**i* + *a**j* is a power of 2 (i. e. some integer *x* exists so that *a**i* + *a**j* = 2*x*).

#### Input

The first line contains the single positive integer *n* (1 ≤ *n* ≤ 105) — the number of integers.

The second line contains *n* positive integers *a*1, *a*2, ..., *a**n* (1 ≤ *a**i* ≤ 109).

#### Output

Print the number of pairs of indexes *i*, *j* (*i* < *j*) that *a**i* + *a**j* is a power of 2.

#### Examples

input

```
4
7 3 2 1

```

output

```
2

```

input

```
3
1 1 1
```

output

```
3

```

#### Note

In the first example the following pairs of indexes include in answer: (1, 4) and (2, 4).

In the second example all pairs of indexes (*i*, *j*) (where *i* < *j*) include in answer.