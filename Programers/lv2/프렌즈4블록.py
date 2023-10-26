# https://school.programmers.co.kr/learn/courses/30/lessons/17679
# [1차] 프렌즈4블록

# 블라인드 공채를 통과한 신입 사원 라이언은 신규 게임 개발 업무를 맡게 되었다. 이번에 출시할 게임 제목은 "프렌즈4블록".
# 같은 모양의 카카오프렌즈 블록이 2×2 형태로 4개가 붙어있을 경우 사라지면서 점수를 얻는 게임이다.
# 각 문자는 라이언(R), 무지(M), 어피치(A), 프로도(F), 네오(N), 튜브(T), 제이지(J), 콘(C)을 의미한다
# 입력으로 블록의 첫 배치가 주어졌을 때, 지워지는 블록은 모두 몇 개인지 판단하는 프로그램을 제작하라.

# 입력 형식
# 입력으로 판의 높이 m, 폭 n과 판의 배치 정보 board가 들어온다.
# 2 ≦ n, m ≦ 30
# board는 길이 n인 문자열 m개의 배열로 주어진다. 블록을 나타내는 문자는 대문자 A에서 Z가 사용된다.

# 출력 형식
# 입력으로 주어진 판 정보를 가지고 몇 개의 블록이 지워질지 출력하라.

m, n = 4, 5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
# answer = 14


# 2차 수정 : 모듈화
def rotate_board_90(board, m, n):
    rotated = [[None] * m for _ in range(n)]
    for y in range(m):
        for x in range(n):
            rotated[x][m - 1 - y] = board[y][x]
    return rotated

def find_blocks_to_remove(board, m, n):
    to_remove = set()
    for y in range(m - 1):
        for x in range(n - 1):
            if board[y][x] == board[y + 1][x] == board[y][x + 1] == board[y + 1][x + 1] != "":
                to_remove.update({(y, x), (y + 1, x), (y, x + 1), (y + 1, x + 1)})
    return to_remove

def remove_blocks(board, blocks, m, n):
    remove_block_cnt = len(blocks)
    for y, x in blocks:
        board[y][x] = ''
    for y, row in enumerate(board):
        board[y] = [i for i in row if i != '']
        board[y].extend([''] * (n - len(board[y])))
    return remove_block_cnt

def solution(m, n, board):
    rotated_board = rotate_board_90(board, m, n)
    m, n = n, m
    total_removed = 0
    while True:
        blocks = find_blocks_to_remove(rotated_board, m, n)
        if not blocks:
            break
        total_removed += remove_blocks(rotated_board, blocks, m, n)
    return total_removed
# 44.52ms, 10.4MB


# 1차 수정 : 로직 변경 및 모듈화
def find_blocks_to_remove(board, m, n):
    to_remove = set()
    for y in range(m - 1):
        for x in range(n - 1):
            if board[y][x] == board[y + 1][x] == board[y][x + 1] == board[y + 1][x + 1] != "":
                to_remove.update({(y, x), (y + 1, x), (y, x + 1), (y + 1, x + 1)})
    return to_remove

def remove_blocks(board, blocks, m, n):
    remove_block_cnt = 0
    for y, x in blocks:
        board[y][x] = ""
    remove_block_cnt += len(blocks)
    for x in range(n):
        col = [board[y][x] for y in range(m) if board[y][x] != ""]
        for y in range(m - len(col)):
            board[y][x] = ""
        for y in range(m - len(col), m):
            board[y][x] = col[y - (m - len(col))]
    return remove_block_cnt

def solution(m, n, board):
    board = [list(row) for row in board]
    total_removed = 0
    while True:
        blocks = find_blocks_to_remove(board, m, n)
        if not blocks:
            break
        total_removed += remove_blocks(board, blocks, m, n)
    return total_removed
# 73.54ms, 10.2MB



# 초기 코드
def solution(m, n, board):
    answer = 0
    arr = []
    for x in range(n):
        char = []
        for y in range(m):
            char.append(board[m - y - 1][x])
        arr.append(char)
    directions = [(1, 0), (0, 1), (1, 1)]
    while True:
        visited = set()
        row = len(arr)
        for y in range(row - 1):
            col = len(arr[y])
            for x in range(col - 1):
                character = arr[y][x]
                temp_arr = [(y, x)]
                for dy, dx in directions:
                    ny = y + dy
                    nx = x + dx
                    if (
                        0 <= ny < row
                        and 0 <= nx < len(arr[ny])
                        and arr[ny][nx] == character
                    ):
                        temp_arr.append((ny, nx))
                if len(temp_arr) == 4:
                    for ny, nx in temp_arr:
                        visited.add((ny, nx))
        for y, row in enumerate(arr):
            arr[y] = [value for x, value in enumerate(row) if (y, x) not in visited]
        if not visited:
            break
        answer += len(visited)
    return answer
# 92.57ms, 10MB


print(solution(m, n, board))


# def solution(m, n, board):
#     answer = 0
#     arr = []
#     for x in range(n):
#         char = []
#         for y in range(m):
#             char.append(board[m - y - 1][x])
#         arr.append(char)

#     directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

#     while True:
#         visited = set()
#         row = len(arr)
#         for y in range(row):
#             col = len(arr[y])
#             for x in range(col):
#                 if (y, x) not in visited:
#                     character = arr[y][x]
#                     queue = deque([(y, x)])
#                     temp_arr = []
#                     while queue:
#                         current_y, current_x = queue.popleft()
#                         for dy, dx in directions:
#                             ny = current_y + dy
#                             nx = current_x + dx
#                             if 0 <= ny < row:
#                                 n_col = len(arr[ny])
#                             else:
#                                 continue
#                             if (
#                                 0 <= nx < n_col
#                                 and (ny, nx) not in visited
#                                 and arr[ny][nx] == character
#                             ):
#                                 temp_arr.append((ny, nx))
#                                 queue.append((ny, nx))
#                                 visited.add((ny, nx))
#                     if len(temp_arr) >= 4:
#                         answer += len(temp_arr)
#                         print(temp_arr)
#                         for ny, nx in temp_arr:
#                             arr[ny][nx] = "X"
#         is_change = False
#         for n in range(row):
#             temp_arr = []
#             for char in arr[n]:
#                 if char != "X":
#                     temp_arr.append(char)
#                 else:
#                     is_change = True
#             arr[n] = temp_arr
#         if not is_change:
#             break
#     return answer
