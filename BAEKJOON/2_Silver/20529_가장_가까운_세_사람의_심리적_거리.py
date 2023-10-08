# https://www.acmicpc.net/problem/20529
# 가장 가까운 세 사람의 심리적 거리

# 문제
# MBTI 성격 유형을 이용하면 두 사람 사이의 심리적인 거리를 정의할 수 있다. 이는 두 사람의 MBTI 유형에서 서로 다른 분류에 속하는 척도의 수로 정의된다. 예를 들어, MBTI 유형이 ISTJ인 사람과 ISFJ인 사람 사이의 거리는 1이며, INTP인 사람과 ENTJ인 사람 사이의 거리는 2이다.
# 이 정의를 확장해서 세 사람 사이의 심리적인 거리도 정의할 수 있다. 세 사람
# A, B, C가 있을 때 이들의 심리적인 거리는
# (A와 B 사이의 심리적인 거리) + (B와 C 사이의 심리적인 거리) + (A와 C 사이의 심리적인 거리)
# 로 정의한다.
# 대학교에서 심리학 교수로 일하는 종서는 자신이 가르치는 학생들의 심리적인 특성을 분석하고 싶어한다.
# 오늘이 생일인 종서를 위해 N명의 학생들의 MBTI 유형이 주어질 때, 가장 가까운 세 학생 사이의 심리적인 거리를 구해보자.

# 입력
# 첫 줄에는 테스트 케이스의 수를 나타내는 정수 T가 주어진다.
# 각 테스트 케이스의 첫 줄에는 학생의 수를 나타내는 하나의 정수 N이 주어지며, 두 번째 줄에는 각 학생의 MBTI 성격 유형을 나타내는 문자열들이 사이에 공백을 두고 주어진다.

# 출력
# 각 테스트 케이스에 대한 답을 정수 형태로 한 줄에 하나씩 출력한다.


# 2차 수정 : 리팩토링
from itertools import combinations
from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    n = int(input())
    if n >= 33:
        input()
        print(0)
        continue
    students = input().split()
    min_dist = float("inf")
    for x, y, z in combinations(students, 3):
        distance = 0
        for i, j, k in zip(x, y, z):
            distance += (i != j) + (j != k) + (k != i)
        min_dist = min(min_dist, distance)
    print(min_dist)
# 31876KB, 432ms, 478B


# 1차 수정 : 조기 종료
from itertools import combinations
from sys import stdin

input = stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    if n >= 33:
        input().split()
        print(0)
        continue
    students = input().split()
    distance = 0
    min_dist = float("inf")
    for x, y, z in combinations(students, 3):
        for i, j in zip(x, y):
            if i != j:
                distance += 1
        for i, j in zip(x, z):
            if i != j:
                distance += 1
        for i, j in zip(z, y):
            if i != j:
                distance += 1
        min_dist = min(min_dist, distance)
        distance = 0
    print(min_dist)
# 38672KB, 648ms, 670B


# 초기 코드
from collections import Counter
from itertools import combinations
from sys import stdin

input = stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    students = Counter(input().split())
    mbtis = []
    for key, cnt in students.items():
        if 3 <= cnt:
            mbtis.extend([key] * 3)
        elif 0 < cnt < 3:
            mbtis.extend([key] * cnt)
        
    distance = 0
    min_dist = float("inf")
    for x, y, z in combinations(mbtis, 3):
        for i, j in zip(x, y):
            if i != j:
                distance += 1
        for i, j in zip(x, z):
            if i != j:
                distance += 1
        for i, j in zip(z, y):
            if i != j:
                distance += 1
        min_dist = min(min_dist, distance)
        distance = 0

    print(min_dist)
# 39276KB, 2352ms, 818B
