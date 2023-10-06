# https://www.acmicpc.net/problem/5525
# IOIOI

# 문제
# N+1개의 I와 N개의 O로 이루어져 있으면, I와 O이 교대로 나오는 문자열을 PN이라고 한다.

# P1 IOI
# P2 IOIOI
# P3 IOIOIOI
# PN IOIOI...OI (O가 N개)
# I와 O로만 이루어진 문자열 S와 정수 N이 주어졌을 때, S안에 PN이 몇 군데 포함되어 있는지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N이 주어진다. 둘째 줄에는 S의 길이 M이 주어지며, 셋째 줄에 S가 주어진다.

# 출력
# S에 PN이 몇 군데 포함되어 있는지 출력한다.

# 1차 수정 : 로직 변경
from sys import stdin
input = stdin.readline

n = int(input())
m = int(input())
s = input().rstrip('\n')

cnt = 0
answer = 0
i = 1
while i < m -1:
    if s[i-1] == 'I' and s[i] == 'O' and s[i+1] == 'I':
        cnt += 1
        if cnt == n:
            answer += 1
            cnt -= 1
        i += 2
    else:
        cnt = 0
        i += 1
print(answer)
# 33212KB, 308ms, 355B

# 초기 코드 : 부분 성공
from sys import stdin
input = stdin.readline

n = int(input())
m = int(input())
s = input().rstrip('\n')

p = "O".join(list("I" * (n + 1)))
len_p = 2 * n + 1
switch = True
cnt = 0
ioi = ""

for char in s:
    if switch:
        if char == "I":
            switch = not switch
            ioi += char
        else:
            if len(ioi) >= len_p:
                cnt += (len(ioi) - len_p) // 2 + 1
            ioi = ""
    else:
        if char == "O":
            switch = not switch
            ioi += char
        else:
            if len(ioi) >= len_p:
                cnt += (len(ioi) - len_p) // 2 + 1
            ioi = "I"

if len(ioi) >= len_p:
    cnt += (len(ioi) - len_p) // 2 + 1

print(cnt)
