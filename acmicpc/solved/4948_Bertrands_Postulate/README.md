# [베르트랑 공준](https://www.acmicpc.net/problem/4948)



| 시간 제한 | 메모리 제한 | 제출   | 정답   | 맞은 사람 | 정답 비율   |
| ----- | ------ | ---- | ---- | ----- | ------- |
| 1 초   | 128 MB | 1904 | 944  | 797   | 52.365% |

## 문제

베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다.

이 명제는 조제프 베르트랑이 1845년에 추측했고, 파프누티 체비쇼프가 1850년에 증명했다.

예를 들어, 10보다 크고, 20보다 작거나 같은 소수는 4개가 있다. (11, 13, 17, 19) 또, 14보다 크고, 28보다 작거나 같은 소수는 3개가 있다. (17,19, 23)

n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오. 

## 입력

입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 케이스는 n을 포함하며, 한 줄로 이루어져 있다. (n ≤ 123456)

입력의 마지막에는 0이 주어진다.

## 출력

각 테스트 케이스에 대해서, n보다 크고, 2n보다 작거나 같은 소수의 개수를 출력한다.

## 예제 입력 복사

```
1
10
13
100
1000
10000
100000
0

```

## 예제 출력 복사

```
1
4
3
21
135
1033
8392

```

## 힌트

## 출처

[ACM-ICPC ](https://www.acmicpc.net/category/1)> [Regionals ](https://www.acmicpc.net/category/7)> [Asia ](https://www.acmicpc.net/category/42)> [Japan ](https://www.acmicpc.net/category/43)> [Domestic Contest ](https://www.acmicpc.net/category/44)> [2011 Domestic Contest](https://www.acmicpc.net/category/detail/201) A번

- 문제를 번역한 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)

## 알고리즘 분류

- [에라토스테네스의 체](https://www.acmicpc.net/problem/tag/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98%20%EC%B2%B4)
- [구현](https://www.acmicpc.net/problem/tag/%EA%B5%AC%ED%98%84)