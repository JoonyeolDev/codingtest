# https://school.programmers.co.kr/learn/courses/30/lessons/181870
# ad 제거하기

# 문제 설명
# 문자열 배열 strArr가 주어집니다. 배열 내의 문자열 중 "ad"라는 부분 문자열을 포함하고 있는 모든 문자열을 제거하고 남은 문자열을 순서를 유지하여 배열로 return 하는 solution 함수를 완성해 주세요.

# 제한사항
# 1 ≤ strArr의 길이 ≤ 1,000
# 1 ≤ strArr의 원소의 길이 ≤ 20
# strArr의 원소는 알파벳 소문자로 이루어진 문자열입니다.

strArr = ["and","notad","abcd"]
# result = ["and","abcd"]

def solution(strArr):
    return [string for string in strArr if not 'ad' in string]