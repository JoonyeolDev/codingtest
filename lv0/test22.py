# https://school.programmers.co.kr/learn/courses/30/lessons/120812
# 최빈값 구하기

# 문제 설명
# 최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다. 
# 정수 배열 array가 매개변수로 주어질 때, 
# 최빈값을 return 하도록 solution 함수를 완성해보세요. 
# 최빈값이 여러 개면 -1을 return 합니다.

# 제한사항
# 0 < array의 길이 < 100
# 0 ≤ array의 원소 < 1000

array = [1, 2, 3, 3, 3, 4]
a = []
arr = list(set(array))
for i in arr:
    a.append([array.count(i), i])
a.sort(reverse=True)
if len(a)==1: answer = a[0][1]
else: 
    if a[0][0]==a[1][0]: answer = -1
    else : answer = a[0][1]

print(answer)

def solution(array):
    a = []
    arr = list(set(array))
    for i in arr:
        a.append([array.count(i), i])
    a.sort(reverse=True)
    if len(a)==1: answer = a[0][1]
    else: 
        if a[0][0]==a[1][0]: answer = -1
        else : answer = a[0][1]
    return answer

def solution1(array):
    a = []
    arr = list(set(array))
    for i in arr:
        a.append([array.count(i), i])
    a.sort(reverse=True)
    if len(a)==1: answer = a[0][1]
    elif a[0][0]==a[1][0]: answer = -1
    else : answer = a[0][1]
    return answer

print(solution1(array))