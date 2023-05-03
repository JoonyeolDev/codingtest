# https://school.programmers.co.kr/learn/courses/30/lessons/120911
# 문자열 정렬하기 (2)

# 문제 설명
# 영어 대소문자로 이루어진 문자열 my_string이 매개변수로 주어질 때, 
# my_string을 모두 소문자로 바꾸고 알파벳 순서대로 정렬한 문자열을 
# return 하도록 solution 함수를 완성해보세요.

# 제한사항
# 0 < my_string 길이 < 100

my_string = "Bcad"

my_string = [i for i in my_string.lower()]
my_string.sort()
answer = ''.join(my_string)
print(answer)

# 제출용 함수
def solution(my_string):
    my_string = [i for i in my_string.lower()]
    my_string.sort()
    answer = ''.join(my_string)
    return answer