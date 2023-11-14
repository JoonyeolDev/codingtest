# https://www.acmicpc.net/problem/1629
# 곱셈

# 문제
# 자연수 A를 B번 곱한 수를 알고 싶다. 단 구하려는 수가 매우 커질 수 있으므로 이를 C로 나눈 나머지를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 A, B, C가 빈 칸을 사이에 두고 순서대로 주어진다. A, B, C는 모두 2,147,483,647 이하의 자연수이다.

# 출력
# 첫째 줄에 A를 B번 곱한 수를 C로 나눈 나머지를 출력한다.

from sys import stdin
input = stdin.readline

a, b, c = map(int, input().split())

def custom_mod(a, b, c):
    if b == 0:
        return 1

    half = custom_mod(a, b // 2, c)

    if b % 2 == 0:
        return (half * half) % c
    else:
        return ((half * half) % c * a) % c

print(custom_mod(a, b, c))
# 31120KB, 40ms, 310B