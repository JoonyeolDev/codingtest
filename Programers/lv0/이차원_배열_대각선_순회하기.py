# https://school.programmers.co.kr/learn/courses/30/lessons/181829
# 이차원 배열 대각선 순회하기

# 문제 설명
# 2차원 정수 배열 board와 정수 k가 주어집니다.

# i + j <= k를 만족하는 모든 (i, j)에 대한 board[i][j]의 합을 return 하는 solution 함수를 완성해 주세요.

# 제한사항
# 1 ≤ board의 길이 ≤ 100
# 1 ≤ board[i]의 길이 ≤ 100
# 1 ≤ board[i][j] ≤ 10,000
# 모든 board[i]의 길이는 같습니다.
# 0 ≤ k < board의 길이 + board[i]의 길이

board = [[0, 1, 2],[1, 2, 3],[2, 3, 4],[3, 4, 5]]
k = 2
# result = 8

def solution(board, k):
    return sum(board[i][j] for i in range(len(board)) for j in range(len(board[0])) if i+j <= k)