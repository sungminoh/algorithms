# [소용돌이 예쁘게 출력하기](https://www.acmicpc.net/problem/1022)

| 시간 제한 | 메모리 제한 | 제출   | 정답   | 맞은 사람 | 정답 비율   |
| ----- | ------ | ---- | ---- | ----- | ------- |
| 2 초   | 128 MB | 1153 | 313  | 246   | 32.411% |

## 문제

크기가 무한인 정사각형 모눈종이가 있다. 모눈종이의 각 정사각형은 행과 열의 쌍으로 표현할 수 있다.

이 모눈종이 전체를 양수를 소용돌이 모양으로 채울 것이다. 일단 숫자 1을 0행 0열에 쓴다. 그리고 나서 0행 1열에 숫자 2를 쓴다. 거기서 부터 소용돌이는 반시계 방향으로 시작된다. 다음 숫자는 다음과 같이 채우면 된다.

![img](https://www.acmicpc.net/upload/201003/bbb.png)

이 문제는 위와 같이 채운 것을 예쁘게 출력하면 된다. r1, c1, r2, c2가 입력으로 주어진다. r1, c1은 가장 왼쪽 위 칸이고, r2, c2는 가장 오른쪽 아래 칸이다.

예쁘게 출력한다는 것은 다음과 같이 출력하는 것이다.

1. 출력은 r1행부터 r2행까지 차례대로 출력한다.
2. 각 원소는 공백으로 구분한다.
3. 모든 행은 같은 길이를 가져야 한다.
4. 공백의 길이는 최소로 해야 한다.
5. 모든 숫자의 길이(앞에 붙는 공백을 포함)는 같아야 한다.
6. 만약 수의 길이가 가장 길이가 긴 수보다 작다면, 왼쪽에서부터 공백을 삽입해 길이를 맞춘다.

## 입력

첫째 줄에 r1, c1, r2, c2가 주어진다. 모두 절대값이 5000보다 작거나 같은 정수이고, r2-r1은 0보다 크거나 같고, 49보다 작거나 같으며, c2-c1은 0보다 크거나 같고, 4보다 작거나 같다.

## 출력

r2-r1+1개의 줄에 소용돌이를 예쁘게 출력한다.

## 예제 입력 복사

```
-3 -3 2 0
```

## 예제 출력 복사

```
37 36 35 34
38 17 16 15
39 18  5  4
40 19  6  1
41 20  7  8
42 21 22 23
```

## 힌트

## 출처

- 문제를 번역한 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)
- 빠진 조건을 찾은 사람: [myungwoo](https://www.acmicpc.net/user/myungwoo)

## 알고리즘 분류

- [시뮬레이션](https://www.acmicpc.net/problem/tag/%EC%8B%9C%EB%AE%AC%EB%A0%88%EC%9D%B4%EC%85%98)
- [구현](https://www.acmicpc.net/problem/tag/%EA%B5%AC%ED%98%84)
- [출력](https://www.acmicpc.net/problem/tag/%EC%B6%9C%EB%A0%A5)