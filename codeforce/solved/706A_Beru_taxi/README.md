### [A. Beru-taxi](http://codeforces.com/problemset/problem/706/A)

- time limit per test: 1 second
- memory limit per test: 256 megabytes
- input: standard input
- output: standard output

Vasiliy lives at point (*a*, *b*) of the coordinate plane. He is hurrying up to work so he wants to get out of his house as soon as possible. New app suggested *n* available Beru-taxi nearby. The *i*-th taxi is located at point (*x**i*, *y**i*) and moves with a speed *v**i*.

Consider that each of *n* drivers will move directly to Vasiliy and with a maximum possible speed. Compute the minimum time when Vasiliy will get in any of Beru-taxi cars.

#### Input

The first line of the input contains two integers *a* and *b* ( - 100 ≤ *a*, *b* ≤ 100) — coordinates of Vasiliy's home.

The second line contains a single integer *n* (1 ≤ *n* ≤ 1000) — the number of available Beru-taxi cars nearby.

The *i*-th of the following *n* lines contains three integers *x**i*, *y**i* and *v**i* ( - 100 ≤ *x**i*, *y**i* ≤ 100, 1 ≤ *v**i* ≤ 100) — the coordinates of the *i*-th car and its speed.

It's allowed that several cars are located at the same point. Also, cars may be located at exactly the same point where Vasiliy lives.

#### Output

Print a single real value — the minimum time Vasiliy needs to get in any of the Beru-taxi cars. You answer will be considered correct if its absolute or relative error does not exceed 10 - 6.

Namely: let's assume that your answer is *a*, and the answer of the jury is *b*. The checker program will consider your answer correct, if ![img](http://codeforces.com/predownloaded/c6/2e/c62ea64d4651240724c5ac4779b671c741edec24.png).

#### Examples

input

```
0 0
2
2 0 1
0 2 2

```

output

```
1.00000000000000000000
```

input

```
1 3
3
3 3 2
-2 3 6
-2 7 10

```

output

```
0.50000000000000000000
```

#### Note

In the first sample, first taxi will get to Vasiliy in time 2, and second will do this in time 1, therefore 1 is the answer.

In the second sample, cars 2 and 3 will arrive simultaneously.