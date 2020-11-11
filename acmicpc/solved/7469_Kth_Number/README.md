# [K번째 숫자](https://www.acmicpc.net/problem/7469)

| 시간 제한 | 메모리 제한 | 제출   | 정답   | 맞은 사람 | 정답 비율   |
| ----- | ------ | ---- | ---- | ----- | ------- |
| 2 초   | 128 MB | 2348 | 660  | 358   | 27.730% |

## 문제

현정이는 자료 구조 프로젝트를 하고 있다. 다른 학생들은 프로젝트 주제로 스택, 큐와 같은 기본 자료 구조를 구현하는 주제를 선택했다. 하지만, 현정이는 새로운 자료 구조를 만들었다.

현정이가 만든 자료구조는 배열을 응용하는 것이다. 배열 a[1...n]에는 서로 다른 숫자가 n개 저장되어 있다. 현정이는 여기에 Q(i,j,k)라는 함수를 구현해 모두를 놀라게 할 것이다.

> Q(i,j,k): 배열 a[i...j]를 정렬했을 때, k번째 숫자를 리턴하는 함수

예를 들어, a = (1,5,2,6,3,7,4)인 경우 Q(2,5,3)의 답을 구하는 과정을 살펴보자. a[2...5]는 (5,2,6,3)이고, 이 배열을 정렬하면 (2,3,5,6)이 된다. 정렬한 배열에서 3번째 숫자는 5이다. 따라서 Q(2,5,3)의 리턴값은 5이다.

배열 a가 주어지고, Q함수를 호출한 횟수가 주어졌을 때, 각 함수의 리턴값을 출력하는 프로그램을 작성하시오.

## 입력

첫째 줄에 배열의 크기 n과 함수 Q를 호출한 횟수 m이 주어진다. (1 ≤ n ≤ 100,000, 1 ≤ m ≤ 5,000)

둘째 줄에는 배열에 포함된 정수가 순서대로 주어진다. 각 정수는 절대값이 109를 넘지 않는 정수이다.

다음 m개 줄에는 Q(i,j,k)를 호출할 때 사용한 인자 i,j,k가 주어진다. (1 ≤ i ≤ j ≤ n, 1 ≤ k ≤ j-i+1)

## 출력

Q함수를 호출할 때마다 그 함수의 리턴값을 한 줄에 하나씩 출력한다. 

## 예제 입력 복사

```
7 3
1 5 2 6 3 7 4
2 5 3
4 4 1
1 7 3

```

## 예제 출력 복사

```
5
6
3

```

## 힌트

## 출처

[ACM-ICPC ](https://www.acmicpc.net/category/1)> [Regionals ](https://www.acmicpc.net/category/7)> [Europe ](https://www.acmicpc.net/category/10)> [Northeastern European Regional Contest ](https://www.acmicpc.net/category/11)> [NEERC Subregional Contest ](https://www.acmicpc.net/category/14)> [NEERC Nothern Subregional 2004](https://www.acmicpc.net/category/detail/897) K번

- 문제를 번역한 사람: [baekjoon](https://www.acmicpc.net/user/baekjoon)

## 링크

- [PKU Judge Online](http://poj.org/problem?id=2104)
- [TJU Online Judge](http://acm.tju.edu.cn/toj/showp2722.html)

## 알고리즘 분류

- [세그먼트 트리](https://www.acmicpc.net/problem/tag/%EC%84%B8%EA%B7%B8%EB%A8%BC%ED%8A%B8%20%ED%8A%B8%EB%A6%AC)
- [정렬](https://www.acmicpc.net/problem/tag/%EC%A0%95%EB%A0%AC)