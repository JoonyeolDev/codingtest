# https://school.programmers.co.kr/learn/courses/30/lessons/12949#
# 행렬의 곱셈
# 문제 설명
# 2차원 행렬 arr1과 arr2를 입력받아, arr1에 arr2를 곱한 결과를 반환하는 함수,
# solution을 완성해주세요.

# 제한 조건
# 행렬 arr1, arr2의 행과 열의 길이는 2 이상 100 이하입니다.
# 행렬 arr1, arr2의 원소는 -10 이상 20 이하인 자연수입니다.
# 곱할 수 있는 배열만 주어집니다.

arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
# [[22, 22, 11], [36, 28, 18], [29, 20, 14]]

# 행렬의 길이를 확인
row = len(arr2)
col = len(arr2[0])

# 행과 열의 길이를 바꾼 빈 리스트를 정의
new_list = [[0 for i in range(row)] for j in range(col)]

# 리스트 값 정의
for i in range(row):
    for j in range(col):
        new_list[j][i]=arr2[i][j]

# answer에 각 리스트 곱하기
answer = []
for i in arr1:
    new_row = []
    for j in new_list:
        sum_=0
        for k in range(len(arr1[0])):
            sum_+=i[k]*j[k]
        new_row.append(sum_)
    answer.append(new_row)

print(answer)

def solution(arr1, arr2):
    row = len(arr2)
    col = len(arr2[0])
    new_list = [[0 for i in range(row)] for j in range(col)]
    for i in range(row):
        for j in range(col):
            new_list[j][i]=arr2[i][j]
    answer = []
    for i in arr1:
        new_row = []
        for j in new_list:
            sum_=0
            for k in range(len(arr1[0])):
                sum_+=i[k]*j[k]
            new_row.append(sum_)
        answer.append(new_row)
    return answer

#######################################

# 코드 줄이기
arr2_zip = zip(*arr2)
# list_ = zip(arr1,*arr2)
answer2 = [[sum(a*b for a,b in zip(i,j)) for j in arr2_zip] for i in arr1]
# print(arr1)
# print(list(arr2_zip))
def solution2(arr1, arr2):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*arr2)] for A_row in arr1]

print(answer)