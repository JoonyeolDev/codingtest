# https://school.programmers.co.kr/learn/courses/30/lessons/181830
# 정사각형으로 만들기

# 문제 설명
# 이차원 정수 배열 arr이 매개변수로 주어집니다. arr의 행의 수가 더 많다면 열의 수가 행의 수와 같아지도록 각 행의 끝에 0을 추가하고, 열의 수가 더 많다면 행의 수가 열의 수와 같아지도록 각 열의 끝에 0을 추가한 이차원 배열을 return 하는 solution 함수를 작성해 주세요.

# 제한사항
# 1 ≤ arr의 길이 ≤ 100
# 1 ≤ arr의 원소의 길이 ≤ 100
# arr의 모든 원소의 길이는 같습니다.
# 1 ≤ arr의 원소의 원소 ≤ 1,000

arr = [[572, 22, 37], [287, 726, 384], [85, 137, 292], [487, 13, 876]]
# result = [[572, 22, 37, 0], [287, 726, 384, 0], [85, 137, 292, 0], [487, 13, 876, 0]]


def solution(arr):
    row = len(arr)
    col = len(arr[0])
    if row < col:
        for _ in range(col-row):
            arr.append([0]*col)
    elif row > col:
        for i in range(row):
            arr[i] = arr[i]+[0]*(row-col)
    return arr

