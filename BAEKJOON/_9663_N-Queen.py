# https://www.acmicpc.net/problem/9663
# N-Queen

# 문제
# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N이 주어진다. (1 ≤ N < 15)

# 출력
# 첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.

from sys import stdin
input = stdin.readline

n = int(input())

# 각 행/열에 퀸이 하나씩 있어야함(like sudoku)
# 

chess = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        