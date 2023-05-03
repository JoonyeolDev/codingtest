# https://school.programmers.co.kr/learn/courses/30/lessons/181915
# 글자 이어 붙여 문자열 만들기

# 문제 설명
# 문자열 my_string과 정수 배열 index_list가 매개변수로 주어집니다. 
# my_string의 index_list의 원소들에 해당하는 인덱스의 글자들을 
# 순서대로 이어 붙인 문자열을 return 하는 
# solution 함수를 작성해 주세요.

# 제한사항
# 1 ≤ my_string의 길이 ≤ 1,000
# my_string의 원소는 영소문자로 이루어져 있습니다.
# 1 ≤ index_list의 길이 ≤ 1,000
# 0 ≤ index_list의 원소 < my_string의 길이

my_string = "cvsgiorszzzmrpaqpe"
index_list = [16, 6, 5, 3, 12, 14, 11, 11, 17, 12, 7]
# result = "programmers"

answer = ''
for i in index_list:
    answer+=my_string[i]
print(answer)

# 제출용 함수
def solution(my_string, index_list):
    answer = ''
    for i in index_list:
        answer+=my_string[i]
    return answer
