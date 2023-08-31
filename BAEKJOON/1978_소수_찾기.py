# https://www.acmicpc.net/problem/1978
# 소수 찾기

# 문제
# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

# 입력
# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

# 출력
# 주어진 수들 중 소수의 개수를 출력한다.

from sys import stdin
input = stdin.readline

n = int(input().rstrip('\n'))
arr = [int(num) for num in input().split()]
cnt = 0
for number in arr:
    if number == 2: 
        cnt += 1
        continue
    elif number == 1 or not num % 2: continue
    sqrt_num = int(number**0.5)
    for num in range(3, sqrt_num+1, 2):
        if not number % num : break
    else: cnt += 1
print(cnt)

# 31256KB, 44ms, 387B