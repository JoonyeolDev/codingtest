# https://school.programmers.co.kr/learn/courses/30/lessons/49994
# 방문 길이

# 문제 설명
# 게임 캐릭터를 4가지 명령어를 통해 움직이려 합니다. 명령어는 다음과 같습니다.

# U: 위쪽으로 한 칸 가기
# D: 아래쪽으로 한 칸 가기
# R: 오른쪽으로 한 칸 가기
# L: 왼쪽으로 한 칸 가기

# 캐릭터는 좌표평면의 (0, 0) 위치에서 시작합니다. 
# 좌표평면의 경계는 왼쪽 위(-5, 5), 왼쪽 아래(-5, -5), 오른쪽 위(5, 5), 오른쪽 아래(5, -5)로 이루어져 있습니다.
# 명령어가 매개변수 dirs로 주어질 때, 게임 캐릭터가 처음 걸어본 길의 길이를 구하여 return 하는 solution 함수를 완성해 주세요.

# 제한사항
# dirs는 string형으로 주어지며, 'U', 'D', 'R', 'L' 이외에 문자는 주어지지 않습니다.
# dirs의 길이는 500 이하의 자연수입니다.

dirs = "ULURRDLLU"
# result = 7


# 초기 코드
def solution(dirs):
    dir_dict = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    current_pos = [0, 0]
    visited = set()
    for dir in dirs:
        new_x, new_y = current_pos[0] + dir_dict[dir][0], current_pos[1] + dir_dict[dir][1]
        if -5 <= new_x <= 5 and -5 <= new_y <= 5:
            path = (current_pos[0], current_pos[1], new_x, new_y)
            reverse_path = (new_x, new_y, current_pos[0], current_pos[1])
            visited.add(path)
            visited.add(reverse_path)
            current_pos = [new_x, new_y]
    return len(visited) // 2
# 2.12ms, 10.4MB


