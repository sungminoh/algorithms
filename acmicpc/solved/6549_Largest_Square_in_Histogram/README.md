# [히스토그램에서 가장 큰 직사각형](https://www.acmicpc.net/problem/6549)

| 시간 제한 | 메모리 제한 | 제출   | 정답   | 맞은 사람 | 정답 비율   |
| ----- | ------ | ---- | ---- | ----- | ------- |
| 1 초   | 128 MB | 4852 | 1188 | 802   | 25.997% |

## 문제

히스토그램은 직사각형 여러 개가 아래쪽으로 정렬되어 있는 도형이다. 각 직사각형은 같은 너비를 가지고 있지만, 높이는 서로 다를 수도 있다. 예를 들어, 왼쪽 그림은 높이가 2, 1, 4, 5, 1, 3, 3이고 너비가 1인 직사각형으로 이루어진 히스토그램이다.

![img](https://www.acmicpc.net/upload/images/histogram.png)

히스토그램에서 가장 큰 직사각형을 구하는 프로그램을 작성하시오.

## 입력

입력은 테스트 케이스 여러 개로 이루어져 있다. 각 테스트 케이스는 한 줄로 이루어져 있고, 직사각형의 수 n이 가장 처음으로 주어진다. (1 ≤ n ≤ 100,000) 그 다음 n개의 정수 h1, ..., hn (0 ≤ hi ≤ 1000000000)가 주어진다. 이 숫자들은 히스토그램에 있는 직사각형의 높이이며, 왼쪽부터 오른쪽까지 순서대로 주어진다. 모든 직사각형의 너비는 1이고, 입력의 마지막 줄에는 0이 하나 주어진다.

## 출력

각 테스트 케이스에 대해서, 히스토그램에서 가장 큰 직사각형의 넓이를 출력한다.

## 예제 입력 복사

```
7 2 1 4 5 1 3 3
4 1000 1000 1000 1000
0

```

## 예제 출력 복사

```
8
4000

```

## 힌트

## 출처

[Contest ](https://www.acmicpc.net/category/45)> [University of Ulm Local Contest ](https://www.acmicpc.net/category/170)> [University of Ulm Local Contest 2003](https://www.acmicpc.net/category/detail/750) H번

- 문제를 번역한 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)
- 데이터를 추가한 사람: [kth004](https://www.acmicpc.net/user/kth004)

## 링크

- [PKU Judge Online](http://poj.org/problem?id=2559)
- [ZJU Online Judge](http://acm.zju.edu.cn/onlinejudge/showProblem.do?problemCode=1985)
- [TJU Online Judge](http://acm.tju.edu.cn/toj/showp1800.html)
- [Sphere Online Judge](http://www.spoj.com/problems/HISTOGRA/)
- [HDU Online Judge](http://acm.hdu.edu.cn/showproblem.php?pid=1506)

## 알고리즘 분류

- [세그먼트 트리](https://www.acmicpc.net/problem/tag/%EC%84%B8%EA%B7%B8%EB%A8%BC%ED%8A%B8%20%ED%8A%B8%EB%A6%AC)
- [스택](https://www.acmicpc.net/problem/tag/%EC%8A%A4%ED%83%9D)
- [분할 정복](https://www.acmicpc.net/problem/tag/%EB%B6%84%ED%95%A0%20%EC%A0%95%EB%B3%B5)