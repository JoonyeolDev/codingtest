# https://school.programmers.co.kr/learn/courses/30/lessons/154538
# 숫자 변환하기

# 문제 설명
# 자연수 x를 y로 변환하려고 합니다. 사용할 수 있는 연산은 다음과 같습니다.

# x에 n을 더합니다
# x에 2를 곱합니다.
# x에 3을 곱합니다.
# 자연수 x, y, n이 매개변수로 주어질 때, x를 y로 변환하기 위해 필요한 최소 연산 횟수를 return하도록 solution 함수를 완성해주세요. 이때 x를 y로 만들 수 없다면 -1을 return 해주세요.

# 제한사항
# 1 ≤ x ≤ y ≤ 1,000,000
# 1 ≤ n < y

x, y, n = 10, 40, 5
x, y, n = 5, 21, 2
# result = 2


# 1차 수정 : 자료구조 변경 및 로직 수정
from collections import deque
def optimized_solution(x, y, n):
    visited = set()
    visited.add(x)
    queue = deque([(x, 0)])
    while queue:
        num, steps = queue.popleft()
        if num == y:
            return steps
        for next_num in [num + n, num * 2, num * 3]:
            if next_num > y:
                continue
            if next_num not in visited:
                visited.add(next_num)
                queue.append((next_num, steps + 1))
    return -1 
# 347.45ms, 58.6MB


# 초기 코드
from collections import deque
def solution(x, y, n):
    visited = [-1] * (y + 1)
    visited[x] = 0
    queue = deque([x])
    while queue:
        num = queue.popleft()
        for next_num in [num + n, num * 2, num * 3]:
            if next_num > y:
                continue
            if visited[next_num] == -1 or visited[next_num] > visited[num] + 1:
                visited[next_num] = visited[num] + 1
                queue.append(next_num)
    return visited[y]
# 540.18ms, 25.8MB


print(solution(x, y, n))
