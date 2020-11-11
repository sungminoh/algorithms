### [A. Letters Cyclic Shift](http://codeforces.com/problemset/problem/708/A)

- time limit per test: 1 second
- memory limit per test: 256 megabytes
- input: standard input
- output: standard output

You are given a non-empty string *s* consisting of lowercase English letters. You have to pick exactly one non-empty substring of *s* and shift all its letters 'z' ![img](http://codeforces.com/predownloaded/9e/58/9e58594e343ae98e6885aaa282186965f4b9653b.png) 'y' ![img](http://codeforces.com/predownloaded/9e/58/9e58594e343ae98e6885aaa282186965f4b9653b.png) 'x' ![img](http://codeforces.com/predownloaded/1b/01/1b01be31aaf100be438d2b4934c93d5d1d32d790.png) 'b' ![img](http://codeforces.com/predownloaded/9e/58/9e58594e343ae98e6885aaa282186965f4b9653b.png) 'a' ![img](http://codeforces.com/predownloaded/9e/58/9e58594e343ae98e6885aaa282186965f4b9653b.png) 'z'. In other words, each character is replaced with the previous character of English alphabet and 'a' is replaced with 'z'.

What is the lexicographically minimum string that can be obtained from *s* by performing this shift exactly once?

#### Input

The only line of the input contains the string *s* (1 ≤ |*s*| ≤ 100 000) consisting of lowercase English letters.

#### Output

Print the lexicographically minimum string that can be obtained from *s* by shifting letters of exactly one non-empty substring.

#### Examples

input

```
codeforces
```

output

```
bncdenqbdr
```

input

```
abacaba
```

output

```
aaacaba
```

#### Note

String *s* is lexicographically smaller than some other string *t* of the same length if there exists some 1 ≤ *i* ≤ |*s*|, such that *s*1 = *t*1, *s*2 = *t*2, ..., *s**i* - 1 = *t**i* - 1, and *s**i* < *t**i*.