# https://www.acmicpc.net/problem/1541
# 헌내기는 친구가 필요해

# 문제
# 2020년에 입학한 헌내기 도연이가 있다. 도연이는 비대면 수업 때문에 학교에 가지 못해 학교에 아는 친구가 없었다. 드디어 대면 수업을 하게 된 도연이는 어서 캠퍼스 내의 사람들과 친해지고 싶다.
# 불쌍한 도연이를 위하여 캠퍼스에서 도연이가 만날 수 있는 사람의 수를 출력하는 프로그램을 작성해보자.

# 입력
# 첫째 줄에는 캠퍼스의 크기를 나타내는 두 정수 N,M이 주어진다.
# 둘째 줄부터 N개의 줄에는 캠퍼스의 정보들이 주어진다. O는 빈 공간, X는 벽, I는 도연이, P는 사람이다. I가 한 번만 주어짐이 보장된다.

# 출력
# 첫째 줄에 도연이가 만날 수 있는 사람의 수를 출력한다. 단, 아무도 만나지 못한 경우 TT를 출력한다.

from collections import deque
from sys import stdin
input = stdin.readline

row, col = map(int, input().split())
campus = []
start = False

for y in range(row):
    info = input().rstrip('\n')
    campus.append(list(info))
    if not start:
        for x, char in enumerate(info):
            if char == 'I':
                start = (y, x)

queue = deque([start])
visited = set([start])
direction = [(1, 0),(-1, 0),(0, 1),(0, -1)]
cnt = 0

while queue:
    current = queue.popleft()
    y, x = current

    for dy, dx in direction:
        ny, nx = y+dy, x+dx
        if 0 <= ny < row and 0 <= nx < col and (ny, nx) not in visited and campus[ny][nx] != 'X':
            visited.add((ny, nx))
            queue.append((ny, nx))
            if campus[ny][nx] == 'P':
                cnt += 1

if not cnt:
    cnt = 'TT'

print(cnt)
# 89036KB, 992ms, 829B
