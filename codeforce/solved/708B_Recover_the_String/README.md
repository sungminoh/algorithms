### [B. Recover the String](http://codeforces.com/problemset/problem/708/B)

- time limit per test: 1 second
- memory limit per test: 256 megabytes
- input: standard input
- output: standard output

For each string *s* consisting of characters '0' and '1' one can define four integers *a*00, *a*01, *a*10 and *a*11, where *a**xy* is the number of subsequences of length 2 of the string *s* equal to the sequence {*x*, *y*}.

In these problem you are given four integers *a*00, *a*01, *a*10, *a*11 and have to find any non-empty string *s* that matches them, or determine that there is no such string. One can prove that if at least one answer exists, there exists an answer of length no more than 1 000 000.

#### Input

The only line of the input contains four non-negative integers *a*00, *a*01, *a*10 and *a*11. Each of them doesn't exceed 109.

#### Output

If there exists a non-empty string that matches four integers from the input, print it in the only line of the output. Otherwise, print "Impossible". The length of your answer must not exceed 1 000 000.

#### Examples

input

```
1 2 3 4

```

output

```
Impossible

```

input

```
1 2 2 1

```

output

```
0110
```