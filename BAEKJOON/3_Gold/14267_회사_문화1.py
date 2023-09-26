# https://www.acmicpc.net/problem/14267
# 회사 문화 1

# 문제
# 영선회사에는 매우 좋은 문화가 있는데, 바로 상사가 직속 부하를 칭찬하면 그 부하가 부하의 직속 부하를 연쇄적으로 칭찬하는 내리 칭찬이 있다. 즉, 상사가 한 직속 부하를 칭찬하면 그 부하의 모든 부하들이 칭찬을 받는다.
# 모든 칭찬에는 칭찬의 정도를 의미하는 수치가 있는데, 이 수치 또한 부하들에게 똑같이 칭찬 받는다.
# 직속 상사와 직속 부하관계에 대해 주어지고, 칭찬에 대한 정보가 주어질 때, 각자 얼마의 칭찬을 받았는지 출력하시오,

# 입력
# 첫째 줄에는 회사의 직원 수 n명, 최초의 칭찬의 횟수 m이 주어진다. 직원은 1번부터 n번까지 번호가 매겨져 있다. (2 ≤ n, m ≤ 100,000)
# 둘째 줄에는 직원 n명의 직속 상사의 번호가 주어진다. 직속 상사의 번호는 자신의 번호보다 작으며, 최종적으로 1번이 사장이다. 1번의 경우, 상사가 없으므로 -1이 입력된다.
# 다음 m줄에는 직속 상사로부터 칭찬을 받은 직원 번호 i, 칭찬의 수치 w가 주어진다. (2 ≤ i ≤ n, 1 ≤ w ≤ 1,000)
# 사장은 상사가 없으므로 칭찬을 받지 않는다.

# 출력
# 1번부터 n번의 직원까지 칭찬을 받은 정도를 출력하시오.

from collections import defaultdict
from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
organization_chart = defaultdict(list)

superior_list = list(map(int, input().split()))
for idx, superior in enumerate(superior_list,1):
    organization_chart[superior].append(idx)

compliment = defaultdict(int)
for _ in range(m):
    i, w = map(int, input().split())
    compliment[i] += w

answer = [0]*(n)

stack = [1]
while stack:
    current = stack.pop()
    for worker in organization_chart[current]:
        answer[worker-1] = answer[current-1] + compliment[worker]
        stack.append(worker)

print(" ".join(map(str, answer)))
# 73512KB, 308ms, 647B