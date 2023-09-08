# https://www.acmicpc.net/problem/1929
# 소수 구하기

# 문제
# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

# 출력
# 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

from sys import stdin
input = stdin.readline

m, n = map(int, input().split())


for number in range(m, n+1):
    if number == 2: 
        print(number)
        continue
    elif number == 1 or not number % 2: continue
    sqrt_num = int(number**0.5)
    for num in range(3, sqrt_num+1, 2):
        if not number % num : break
    else: print(number)

# 31256KB, 2976ms, 347B