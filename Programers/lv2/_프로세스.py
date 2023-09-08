# https://school.programmers.co.kr/learn/courses/30/lessons/42587
# 프로세스

# 문제 설명
# 운영체제의 역할 중 하나는 컴퓨터 시스템의 자원을 효율적으로 관리하는 것입니다. 이 문제에서는 운영체제가 다음 규칙에 따라 프로세스를 관리할 경우 특정 프로세스가 몇 번째로 실행되는지 알아내면 됩니다.

# 1. 실행 대기 큐(Queue)에서 대기중인 프로세스 하나를 꺼냅니다.
# 2. 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 프로세스를 다시 큐에 넣습니다.
# 3. 만약 그런 프로세스가 없다면 방금 꺼낸 프로세스를 실행합니다.
#   3.1 한 번 실행한 프로세스는 다시 큐에 넣지 않고 그대로 종료됩니다.
# 예를 들어 프로세스 4개 [A, B, C, D]가 순서대로 실행 대기 큐에 들어있고, 우선순위가 [2, 1, 3, 2]라면 [C, D, A, B] 순으로 실행하게 됩니다.

# 현재 실행 대기 큐(Queue)에 있는 프로세스의 중요도가 순서대로 담긴 배열 priorities와, 몇 번째로 실행되는지 알고싶은 프로세스의 위치를 알려주는 location이 매개변수로 주어질 때, 해당 프로세스가 몇 번째로 실행되는지 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# priorities의 길이는 1 이상 100 이하입니다.
# priorities의 원소는 1 이상 9 이하의 정수입니다.
# priorities의 원소는 우선순위를 나타내며 숫자가 클 수록 우선순위가 높습니다.
# location은 0 이상 (대기 큐에 있는 프로세스 수 - 1) 이하의 값을 가집니다.
# priorities의 가장 앞에 있으면 0, 두 번째에 있으면 1 … 과 같이 표현합니다.

priorities = [2, 1, 3, 2]
priorities = [1, 1, 9, 1, 1, 1]
location = 2
location = 0


# 1차 수정 : 로직 변경
def solution(priorities, location):
    queue = deque([(value, idx) for idx, value in enumerate(priorities)])
    sorted_priorities = deque(sorted(priorities, reverse=True))
    cnt = 0
    while queue:
        current = queue.popleft()
        if current[0] == sorted_priorities[0]:
            cnt += 1
            sorted_priorities.popleft()
            if current[1] == location:
                return cnt
        else:
            queue.append(current)
# 0.12ms, 10.3MB


# 초기 코드
from collections import deque
def solution(priorities, location):
    priorities = [[value, idx] for idx, value in enumerate(priorities)]
    priorities = deque(priorities)
    answer = 0
    while True:
        peak = priorities.popleft()
        if priorities and peak[0] < max(priorities)[0]:
            priorities.append(peak)
        else:
            answer += 1
            if peak[1]==location:
                return answer
# 1.34ms, 10.2MB