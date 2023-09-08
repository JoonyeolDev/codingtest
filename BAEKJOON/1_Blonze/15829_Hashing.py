# https://www.acmicpc.net/problem/15829
# Hashing

# 입력
# 첫 줄에는 문자열의 길이 L이 들어온다. 둘째 줄에는 영문 소문자로만 이루어진 문자열이 들어온다.
# 입력으로 주어지는 문자열은 모두 알파벳 소문자로만 구성되어 있다.

# 출력
# 문제에서 주어진 해시함수와 입력으로 주어진 문자열을 사용해 계산한 해시 값을 정수로 출력한다.

import sys
input = sys.stdin.readline

n = int(input())
sum_ = 0
for idx, char in enumerate(input().rstrip('\n')):
    sum_ += (ord(char) - 96) * (31 ** idx)
print(sum_ % 1234567891)

# 31256KB, 44ms, 181B