# https://school.programmers.co.kr/learn/courses/30/lessons/181833
# 특별한 이차원 배열 1

# 문제 설명
# 정수 n이 매개변수로 주어질 때, 다음과 같은 n × n 크기의 이차원 배열 arr를 return 하는 solution 함수를 작성해 주세요.

# arr[i][j] (0 ≤ i, j < n)의 값은 i = j라면 1, 아니라면 0입니다.

# 제한사항
# 1 ≤ n ≤ 100

n = 3
# result = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

def solution(n):
    answer = []
    for i in range(n):
        temp = []
        for j in range(n):
            if i==j: temp.append(1)
            else: temp.append(0)
        answer.append(temp)
    return  answer