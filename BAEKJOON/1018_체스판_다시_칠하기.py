# https://www.acmicpc.net/problem/1018
# 체스판 다시 칠하기

# 문제
# 지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M×N 크기의 보드를 찾았다. 어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다. 지민이는 이 보드를 잘라서 8×8 크기의 체스판으로 만들려고 한다.

# 체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다. 따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.

# 보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 8×8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다. 당연히 8*8 크기는 아무데서나 골라도 된다. 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N과 M이 주어진다. N과 M은 8보다 크거나 같고, 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다. B는 검은색이며, W는 흰색이다.

# 출력
# 첫째 줄에 지민이가 다시 칠해야 하는 정사각형 개수의 최솟값을 출력한다.

from sys import stdin
input = stdin.readline
# n, m = map(int,input().split())
# arr = [input().rstrip('\n') for _ in range(n)]

n, m = 10, 13

arr = ['BBBBBBBBWBWBW',
       'BBBBBBBBBWBWB',
       'BBBBBBBBWBWBW',
       'BBBBBBBBBWBWB',
       'BBBBBBBBWBWBW',
       'BBBBBBBBBWBWB',
       'BBBBBBBBWBWBW',
       'BBBBBBBBBWBWB',
       'WWWWWWWWWWBWB',
       'WWWWWWWWWWBWB',
       ]


# 1차 수정 : 로직 변경
min_changes = 64 
start_colors = ['BW', 'WB']
for i in range(n - 7):
    for j in range(m - 7):
        for start_color in start_colors:
            changes_needed = 0
            for y in range(i, i + 8):
                for x in range(j, j + 8):
                    expected_color = start_color[((y - i + x - j) % 2)]
                    if arr[y][x] != expected_color:
                        changes_needed += 1
            min_changes = min(min_changes, changes_needed)

print(min_changes)




# 초기 코드
from sys import stdin
input = stdin.readline
# n, m = map(int,input().split())
# arr = [input().rstrip('\n') for _ in range(n)]
square = {}
for y in range(n):
    base = 'B' if y % 2 else 'W'
    for x in range(m-7):
        char = arr[y][x:x+8]
        cnt = 0
        anti_cnt = 0
        for i,c in enumerate(char):
            if (x+i) % 2:
                if base == c:
                    anti_cnt += 1
                else:
                    cnt += 1
            else:
                if base == c:
                    cnt += 1
                else:
                    anti_cnt += 1
        square[(y,x)] = (cnt, anti_cnt)
min_changes = 64
for i in range(n-7):
    for x in range(m-7):
        cnt = 0
        anti_cnt = 0
        for y in range(i,i+8):
            cnt += square[(y,x)][0]
            anti_cnt += square[(y,x)][1]
    min_changes = min(min_changes,cnt,anti_cnt)
print(min_changes)