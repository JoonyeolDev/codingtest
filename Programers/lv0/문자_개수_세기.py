# https://school.programmers.co.kr/learn/courses/30/lessons/181902
# 문자 개수 세기

# 문제 설명
# 알파벳 대소문자로만 이루어진 문자열 my_string이 주어질 때, my_string에서 'A'의 개수, my_string에서 'B'의 개수,..., my_string에서 'Z'의 개수, my_string에서 'a'의 개수, my_string에서 'b'의 개수,..., my_string에서 'z'의 개수를 순서대로 담은 길이 52의 정수 배열을 return 하는 solution 함수를 작성해 주세요.

# 제한사항
# 1 ≤ my_string의 길이 ≤ 1,000

my_string = "Programmers"
# result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 2, 0, 1, 0, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0]

def solution(my_string):
    alpha_dict = {}
    for i in range(65,123):
        if i not in [num for num in range(91,97)]:
            alpha_dict[chr(i)] = 0
    for string in my_string:
        alpha_dict[string] += 1
    return list(alpha_dict.values())
