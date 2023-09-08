# https://school.programmers.co.kr/learn/courses/30/lessons/148652
# 유사 칸토어 비트열

# 문제 설명
# 수학에서 칸토어 집합은 0과 1 사이의 실수로 이루어진 집합으로, [0, 1]부터 시작하여 각 구간을 3등분하여 가운데 구간을 반복적으로 제외하는 방식으로 만들어집니다.

# 남아는 칸토어 집합을 조금 변형하여 유사 칸토어 비트열을 만들었습니다. 유사 칸토어 비트열은 다음과 같이 정의됩니다.

# 0 번째 유사 칸토어 비트열은 "1" 입니다.
# n(1 ≤ n) 번째 유사 칸토어 비트열은 n - 1 번째 유사 칸토어 비트열에서의 1을 11011로 치환하고 0을 00000로 치환하여 만듭니다.
# 남아는 n 번째 유사 칸토어 비트열에서 특정 구간 내의 1의 개수가 몇 개인지 궁금해졌습니다.
# n과 1의 개수가 몇 개인지 알고 싶은 구간을 나타내는 l, r이 주어졌을 때 그 구간 내의 1의 개수를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ n ≤ 20
# 1 ≤ l, r ≤ 5n
# l ≤ r < l + 10,000,000
# l과 r은 비트열에서의 인덱스(1-base)이며 폐구간 [l, r]을 나타냅니다.

n,l,r = 2,4,17 
# result = 8

# 재귀함수로 풀기
def sol(i):
    if i%5==2:
        return 0
    if i<=4:
        return 1
    return sol(i//5)

def solution(n, l, r):
    answer=0
    for i in range(l-1,r):
        answer+= sol(i)
    return answer

# 일반화 해서 풀기
def dec_to_pen(n,sum=''):
    if n==0: 
        if sum=='': sum='0'
        return sum
    return dec_to_pen(n//5,str(n%5)+sum)

def cantor(i):
    if i <0: 
        return 0
    arr = [1,1,0,1,1]
    sum_cantor = 0
    penta = dec_to_pen(i)
    find_2 = len(penta)-penta.find('2')-1
    for idx, j in enumerate(penta[::-1]):
        if idx==0 and find_2==len(penta):
            sum_cantor += sum(arr[:int(j)+1])
        elif find_2==len(penta) or idx>=find_2:
            sum_cantor += sum(arr[:int(j)])*(4**(idx))
    return sum_cantor

def solution(n, l, r):
    answer=cantor(r-1)-cantor(l-2)
    return answer