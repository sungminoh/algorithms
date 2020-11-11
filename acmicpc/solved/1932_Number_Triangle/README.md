# [숫자삼각형](https://www.acmicpc.net/problem/1932)

| 시간 제한 | 메모리 제한 | 제출    | 정답   | 맞은 사람 | 정답 비율   |
| ----- | ------ | ----- | ---- | ----- | ------- |
| 2 초   | 128 MB | 10200 | 5555 | 4089  | 56.525% |

## 문제

```
        7
      3   8
    8   1   0
  2   7   4   4
4   5   2   6   5
```

위 그림은 크기가 5인 숫자 삼각형의 한 모습이다.

맨 위층 7부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때, 이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성하라. 아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택할 수 있다.

삼각형의 크기는 1 이상 500 이하이다. 삼각형을 이루고 있는 각 숫자는 모두 정수이며, 범위는 0 이상 99 이하이다.

## 입력

첫째 줄에 삼각형의 크기 n(1≤n≤500)이 주어지고, 둘째 줄부터 n+1줄까지 숫자 삼각형이 주어진다.

## 출력

첫째 줄에는 최대가 되는 합을 출력한다.

## 예제 입력 복사

```
5
7
3 8
8 1 0 
2 7 4 4
4 5 2 6 5
```

## 예제 출력 복사

```
30

```

## 힌트

## 출처

[Olympiad ](https://www.acmicpc.net/category/2)> [International Olympiad in Informatics ](https://www.acmicpc.net/category/99)> [IOI 1994](https://www.acmicpc.net/category/detail/541) 1번

- 데이터를 추가한 사람: [hwangtmdals](https://www.acmicpc.net/user/hwangtmdals)
- 문제의 오타를 찾은 사람: [Martian](https://www.acmicpc.net/user/Martian)

## 링크

- [PKU Judge Online](http://poj.org/problem?id=1163)
- [Sphere Online Judge](http://www.spoj.com/problems/SUMITR/)

## 알고리즘 분류

- [다이나믹 프로그래밍](https://www.acmicpc.net/problem/tag/%EB%8B%A4%EC%9D%B4%EB%82%98%EB%AF%B9%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)