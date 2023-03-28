# https://school.programmers.co.kr/learn/courses/30/lessons/120851
# 숨어있는 숫자의 덧셈 (1)

# 문제 설명
# 문자열 my_string이 매개변수로 주어집니다. 
# my_string안의 모든 자연수들의 합을 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ my_string의 길이 ≤ 1,000
# my_string은 소문자, 대문자 그리고 한자리 자연수로만 구성되어있습니다.

my_string = "1a2b3c4d123"

# in으로 조건 만들기
answer = 0
for i in my_string:
    if i in ['1','2','3','4','5','6','7','8','9']:
        answer+=int(i)

# 제출용 함수
def solution(my_string):
    answer = 0
    for i in my_string:
        if i in ['1','2','3','4','5','6','7','8','9']:
            answer+=int(i)
    return answer

# chr와 replace 써보기
def solution2(my_string):
    answer = 0
    for i in range(65,123):
        my_string = my_string.replace(chr(i),"")
    for i in my_string:
        answer +=int(i)
    return answer


