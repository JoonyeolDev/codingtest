# https://www.acmicpc.net/problem/1931
# 회의실 배정

# 문제
# 한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다. 각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자. 단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다. 회의의 시작시간과 끝나는 시간이 같을 수도 있다. 이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.

# 입력
# 첫째 줄에 회의의 수 N(1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N+1 줄까지 각 회의의 정보가 주어지는데 이것은 공백을 사이에 두고 회의의 시작시간과 끝나는 시간이 주어진다. 시작 시간과 끝나는 시간은 231-1보다 작거나 같은 자연수 또는 0이다.

# 출력
# 첫째 줄에 최대 사용할 수 있는 회의의 최대 개수를 출력한다.

# 첫 인덱스부터 ㄱ
# 해당 인덱스를 visited에 넣음
# 다음 인덱스 확인 > for문으로 visited에 있는 인덱스에 해당하는 값들하고 겹치는지 확인
# for문 다 돌때까지 안겹치면 visited에 넣음


# 1차 수정 : 로직 변경
import sys
input = sys.stdin.readline

meetings = []
for _ in range(int(input())):
    meeting = tuple(map(int, input().split()))
    meetings.append(meeting)

meetings.sort(key = lambda x: (x[1], x[0]))
len_meetings = len(meetings)

max_meeting_cnt = 0
last_visited_time =0
for i in range(len_meetings):
    start_time, end_time = meetings[i]
    if last_visited_time <= start_time:
        last_visited_time = end_time
        max_meeting_cnt += 1
print(max_meeting_cnt)
# 52036KB, 252ms, 472B


# 초기 코드 : 시간 초과
import sys
input = sys.stdin.readline

meetings = []
for _ in range(int(input())):
    meeting = tuple(map(int, input().split()))
    meetings.append(meeting)

meetings.sort(key = lambda x: x[1] - x[0])
len_meetings = len(meetings)

max_meeting_cnt = 0
start_idx = 0
for i in range(len_meetings):
    visited = set()
    visited.add(i)
    for j in range(i+1,len_meetings):
        s, e = meetings[j]
        for v in visited:
            first_idx, last_idx = meetings[v]
            if first_idx <= s <= last_idx or first_idx <= e <= last_idx:
                break
        else: visited.add(j)
    max_meeting_cnt = max(max_meeting_cnt, len(visited))

print(max_meeting_cnt)