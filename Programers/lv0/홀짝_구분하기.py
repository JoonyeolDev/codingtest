# https://school.programmers.co.kr/learn/courses/30/lessons/181944
# 홀짝 구분하기

# 문제 설명
# 자연수 n이 입력으로 주어졌을 때 만약 n이 짝수이면 "n is even"을, 홀수이면 "n is odd"를 출력하는 코드를 작성해 보세요.

# 제한사항
# 1 ≤ n ≤ 1,000

a = int(input())

print(a, 'is odd' if a % 2 else 'is even')