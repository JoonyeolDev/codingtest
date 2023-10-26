# https://school.programmers.co.kr/learn/courses/30/lessons/12914?language=python3

# 멀리 뛰기

# 문제 설명
# 효진이는 멀리 뛰기를 연습하고 있습니다. 효진이는 한번에 1칸, 또는 2칸을 뛸 수 있습니다. 칸이 총 4개 있을 때, 효진이는
# (1칸, 1칸, 1칸, 1칸)
# (1칸, 2칸, 1칸)
# (1칸, 1칸, 2칸)
# (2칸, 1칸, 1칸)
# (2칸, 2칸)
# 의 5가지 방법으로 맨 끝 칸에 도달할 수 있습니다. 멀리뛰기에 사용될 칸의 수 n이 주어질 때, 효진이가 끝에 도달하는 방법이 몇 가지인지 알아내, 여기에 1234567를 나눈 나머지를 리턴하는 함수, solution을 완성하세요. 예를 들어 4가 입력된다면, 5를 return하면 됩니다.

# 제한 사항
# n은 1 이상, 2000 이하인 정수입니다.

n = 4
# result = 5


# 1차 수정 : 재귀함수 깊이 제한 > for 수정
def solution(n):
    if n==1: return 1
    elif n==2: return 2
    a, b = 1, 2
    for _ in range(n-1):
        a, b = b, a + b
    return a % 1234567

for i in range(1,10):
    print(solution(i))


# 초기 코드 : 런타임 실패
def solution(n,f=1,s=2,cnt=2):
    if n==1: 
        return f
    elif cnt==n:
        return s%1234567
    return solution(n,s,f+s,cnt+1)
