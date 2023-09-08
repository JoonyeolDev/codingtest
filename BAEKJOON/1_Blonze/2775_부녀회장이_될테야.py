# https://solved.ac/class/2/unsolved
# 부녀회장이 될테야

# 문제
# 이 아파트에 거주를 하려면 조건이 있는데, “a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다” 는 계약 조항을 꼭 지키고 들어와야 한다.
# 아파트에 비어있는 집은 없고 모든 거주민들이 이 계약 조건을 지키고 왔다고 가정했을 때, 주어지는 양의 정수 k와 n에 대해 k층에 n호에는 몇 명이 살고 있는지 출력하라. 단, 아파트에는 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.

# 입력
# 첫 번째 줄에 Test case의 수 T가 주어진다. 그리고 각각의 케이스마다 입력으로 첫 번째 줄에 정수 k, 두 번째 줄에 정수 n이 주어진다

# 출력
# 각각의 Test case에 대해서 해당 집에 거주민 수를 출력하라.

# 제한
# 1 ≤ k, n ≤ 14

from sys import stdin
input = stdin.readline

def population(k, n, cnt=0, arr=None):
    if not arr:
        arr = [i for i in range(1, n+1)]
    if k == cnt:
        return arr[n-1]
    arr = [sum(arr[:i]) for i in range(1, n+1)]
    return population(k, n, cnt+1, arr)

for _ in range(int(input().rstrip('\n'))):
    k = int(input().rstrip('\n'))
    n = int(input().rstrip('\n'))
    print(population(k, n))

# 31256KB, 44ms, 408B