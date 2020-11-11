# [Z](https://www.acmicpc.net/problem/1074)

| 시간 제한 | 메모리 제한 | 제출   | 정답   | 맞은 사람 | 정답 비율   |
| ----- | ------ | ---- | ---- | ----- | ------- |
| 2 초   | 128 MB | 4414 | 2010 | 1127  | 42.609% |

## 문제

한수는 2차원 배열 (항상 2^N * 2^N 크기이다)을 Z모양으로 탐색하려고 한다. 예를 들어, 2*2배열을 왼쪽 위칸, 오른쪽 위칸, 왼쪽 아래칸, 오른쪽 아래칸 순서대로 방문하면 Z모양이다.

![img](https://www.acmicpc.net/upload/201003/z1.JPG)

만약, 2차원 배열의 크기가 2^N * 2^N라서 왼쪽 위에 있는 칸이 하나가 아니라면, 배열을 4등분 한 후에 (크기가 같은 2^(N-1)로) 재귀적으로 순서대로 방문한다.

다음 예는 2^2 * 2^2 크기의 배열을 방문한 순서이다.

![img](https://www.acmicpc.net/upload/201003/z2.JPG)

N이 주어졌을 때, (r, c)를 몇 번째로 방문하는지 출력하는 프로그램을 작성하시오.

다음 그림은 N=3일 때의 예이다.

![img](https://www.acmicpc.net/upload/201003/z3.JPG)

## 입력

첫째 줄에 N r c가 주어진다. N은 15보다 작거나 같은 자연수이고, r과 c는 0보다 크거나 같고, 2^N-1보다 작거나 같은 정수이다

## 출력

첫째 줄에 문제의 정답을 출력한다.

## 예제 입력 복사

```
2 3 1

```

## 예제 출력 복사

```
11

```

## 예제 입력 2 복사

```
3 7 7

```

## 예제 출력 2 복사

```
63

```

## 힌트

## 출처

- 문제를 번역한 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)
- 잘못된 조건을 찾은 사람: [hmw9309](https://www.acmicpc.net/user/hmw9309)

## 알고리즘 분류

- [수학](https://www.acmicpc.net/problem/tag/%EC%88%98%ED%95%99)
- [분할 정복](https://www.acmicpc.net/problem/tag/%EB%B6%84%ED%95%A0%20%EC%A0%95%EB%B3%B5)
- [재귀 호출](https://www.acmicpc.net/problem/tag/%EC%9E%AC%EA%B7%80%20%ED%98%B8%EC%B6%9C)