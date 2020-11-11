# [크로아티아 알파벳](https://www.acmicpc.net/problem/2941)



| 시간 제한 | 메모리 제한 | 제출   | 정답   | 맞은 사람 | 정답 비율   |
| ----- | ------ | ---- | ---- | ----- | ------- |
| 1 초   | 128 MB | 3415 | 1265 | 1122  | 39.591% |

## 문제

예전에는 운영체제에서 크로아티아 알파벳을 입력할 수가 없었다. 따라서, 다음과 같이 크로아티아 알파벳을 다음과 같이 변경해서 입력했다.

| 크로아티아 알파벳 | 변경   |
| --------- | ---- |
| č         | c=   |
| ć         | c-   |
| dž        | dz=  |
| ñ         | d-   |
| lj        | lj   |
| nj        | nj   |
| š         | s=   |
| ž         | z=   |

예를 들어, ljes=njak은 크로아티아 알파벳 6개(lj, e, š, nj, a, k)로 이루어져 있다.

단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.

## 입력

첫째 줄에 최대 100글자의 단어가 주어진다. 알파벳 소문자와 '-', '='로만 이루어져 있다.

문제 설명에 나와있는 크로아티아 알파벳만 주어진다.

## 출력

입력으로 주어진 단어가 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.

## 예제 입력 복사

```
ljes=njak

```

## 예제 출력 복사

```
6

```

## 힌트

## 출처

[Contest ](https://www.acmicpc.net/category/45)> [Croatian Open Competition in Informatics ](https://www.acmicpc.net/category/17)> [COCI 2008/2009 ](https://www.acmicpc.net/category/22)> [Contest #5](https://www.acmicpc.net/category/detail/96) 1번

- 문제를 번역한 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)
- 데이터를 추가한 사람: [handong](https://www.acmicpc.net/user/handong) [veydpz](https://www.acmicpc.net/user/veydpz) [zzangho](https://www.acmicpc.net/user/zzangho)

## 알고리즘 분류

- [문자열 처리](https://www.acmicpc.net/problem/tag/%EB%AC%B8%EC%9E%90%EC%97%B4%20%EC%B2%98%EB%A6%AC)