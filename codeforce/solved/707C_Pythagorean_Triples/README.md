### [C. Pythagorean Triples](http://codeforces.com/problemset/problem/707/C)

- time limit per test: 1 second
- memory limit per test: 256 megabytes
- input: standard input
- output: standard output

Katya studies in a fifth grade. Recently her class studied right triangles and the Pythagorean theorem. It appeared, that there are triples of positive integers such that you can construct a right triangle with segments of lengths corresponding to triple. Such triples are called Pythagorean triples.

For example, triples (3, 4, 5), (5, 12, 13) and (6, 8, 10) are Pythagorean triples.

Here Katya wondered if she can specify the length of some side of right triangle and find any Pythagorean triple corresponding to such length? Note that the side which length is specified can be a cathetus as well as hypotenuse.

Katya had no problems with completing this task. Will you do the same?

#### Input

The only line of the input contains single integer *n* (1 ≤ *n* ≤ 109) — the length of some side of a right triangle.

#### Output

Print two integers *m* and *k* (1 ≤ *m*, *k* ≤ 1018), such that *n*, *m* and *k* form a Pythagorean triple, in the only line.

In case if there is no any Pythagorean triple containing integer *n*, print  - 1 in the only line. If there are many answers, print any of them.

#### Examples

input

```
3
```

output

```
4 5
```

input

```
6
```

output

```
8 10
```

input

```
1
```

output

```
-1
```

input

```
17
```

output

```
144 145
```

input

```
67
```

output

```
2244 2245
```

#### Note

![img](http://codeforces.com/predownloaded/1e/c5/1ec504abd66f20b75c88d3f4f370b3724f1e4e28.png)

Illustration for the first sample.