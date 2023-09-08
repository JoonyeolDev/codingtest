# https://school.programmers.co.kr/learn/courses/30/lessons/181832
# 정수를 나선형으로 배치하기

# 문제 설명
# 양의 정수 n이 매개변수로 주어집니다. n × n 배열에 1부터 n2 까지 정수를 인덱스 [0][0]부터 시계방향 나선형으로 배치한 이차원 배열을 return 하는 solution 함수를 작성해 주세요.

# 제한사항
# 1 ≤ n ≤ 30

n = 4
# result = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]

def solution(n):
    answer = [[0] * n for _ in range(n)]
    start_idx = 0
    end_idx = n-1
    num = 1
    while start_idx <= end_idx:
        for i in range(start_idx,end_idx+1):
            answer[start_idx][i] = num
            num += 1
        for i in range(start_idx+1,end_idx+1):
            answer[i][end_idx] = num
            num += 1
        for i in range(end_idx-1,start_idx-1,-1):
            answer[end_idx][i] = num
            num += 1
        for i in range(end_idx-1,start_idx,-1):
            answer[i][start_idx] = num
            num += 1
        start_idx += 1
        end_idx -= 1
    return answer


