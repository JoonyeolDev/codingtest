# https://school.programmers.co.kr/learn/courses/30/lessons/68935
# 문제 설명
# 자연수 n이 매개변수로 주어집니다. n을 3진법 상에서 앞뒤로 뒤집은 후, 
# 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# n은 1 이상 100,000,000 이하인 자연수입니다.

n = 125
# result = 7

# 재귀함수로 3진법 > 10진법 후 리버스
def dec_to_tri_reversed(number,str_tri=''):
    if number==0: return str_tri
    return dec_to_tri_reversed(number//3,str_tri+str(number%3))

# 재귀함수로 3진법 > 10진법
def tri_to_dec(str_tri, number=0,idx=0):
    if idx==len(str_tri): return number
    return tri_to_dec(str_tri, number+(3**idx)*int(str_tri[len(str_tri)-idx-1]),idx+1)

answer = tri_to_dec(dec_to_tri_reversed(n), number=0,idx=0)

print(answer)

# 제출용 함수
def solution(n):
    answer = tri_to_dec(dec_to_tri_reversed(n), number=0,idx=0)
    return answer