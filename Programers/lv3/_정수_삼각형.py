# https://school.programmers.co.kr/learn/courses/30/lessons/43105
# 정수 삼각형

# 위와 같은 삼각형의 꼭대기에서 바닥까지 이어지는 경로 중, 거쳐간 숫자의 합이 가장 큰 경우를 찾아보려고 합니다. 아래 칸으로 이동할 때는 대각선 방향으로 한 칸 오른쪽 또는 왼쪽으로만 이동 가능합니다. 예를 들어 3에서는 그 아래칸의 8 또는 1로만 이동이 가능합니다.
# 삼각형의 정보가 담긴 배열 triangle이 매개변수로 주어질 때, 거쳐간 숫자의 최댓값을 return 하도록 solution 함수를 완성하세요.

# 제한사항
# 삼각형의 높이는 1 이상 500 이하입니다.
# 삼각형을 이루고 있는 숫자는 0 이상 9,999 이하의 정수입니다.

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]


# 1차 수정 : 로직 변경
def solution(triangle):
    n = len(triangle)
    dp = triangle[-1].copy()
    for i in range(n - 2, -1, -1):
        for j in range(len(triangle[i])):
            dp[j] = triangle[i][j] + max(dp[j], dp[j + 1])
    return dp[0]
# 45.59ms, 13.9MB


# 초기 코드
def solution(triangle):
    arr = [0] * len(triangle[-1])
    arr[0] = triangle[0][0]
    for h in range(len(triangle) - 1):
        temp_arr = arr.copy()
        for idx in range(len(triangle[h])):
            arr[idx] = max(arr[idx], temp_arr[idx] + triangle[h+1][idx])
            arr[idx + 1] = max(arr[idx + 1], temp_arr[idx] + triangle[h+1][idx+1])
    return max(arr)
# 73.18ms, 14.6MB