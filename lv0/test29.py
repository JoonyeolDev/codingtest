# https://school.programmers.co.kr/learn/courses/30/lessons/120850
# 문자열 정렬하기 (1)

# 문제 설명
# 문자열 my_string이 매개변수로 주어질 때, 
# my_string 안에 있는 숫자만 골라 오름차순 정렬한 리스트를 
# return 하도록 solution 함수를 작성해보세요.

# 제한사항
# 1 ≤ my_string의 길이 ≤ 100
# my_string에는 숫자가 한 개 이상 포함되어 있습니다.
# my_string은 영어 소문자 또는 0부터 9까지의 숫자로 이루어져 있습니다.

my_string = "p2o4i8gj2"

# isnumeric으로 숫자인지 확인 후 맞으면 asnwer에 추가
answer = []
for i in my_string:
    if i.isnumeric() : answer.append(int(i))
answer.sort()
print(answer)

# 제출용 함수
def solution(my_string):
    answer = []
    for i in my_string:
        if i.isnumeric()==True: answer.append(int(i))
    answer.sort()
    return answer

# 풀었던 문제 다른방법으로 풀기
# try - except로 풀면 어떨까?
answer = []
for i in my_string:
    try:
        answer.append(int(i))
    except:
        pass
answer.sort()
print(answer)

# 제출용 함수
def solution(my_string):
    answer = []
    for i in my_string:
        try:
            answer.append(int(i))
        except:
            pass
    answer.sort()
    return answer