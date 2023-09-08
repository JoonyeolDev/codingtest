# https://www.acmicpc.net/problem/15810
# 풍선 공장

# 문제
# 전북대학교 프로그래밍 경진 대회에서는 ACM-ICPC 스타일을 따라 문제를 해결한 팀에게 그 문제에 해당하는 풍선을 달아준다.

# 풍선을 담당하는 N명의 스태프가 있다. 스태프마다 폐활량이 다르기 때문에 하나의 풍선을 만드는 데 걸리는 시간은 다양하다.

# 대회가 시작되고 운영진으로부터 M개의 풍선을 만들어 달라는 의뢰가 들어왔다!

# 각 스태프가 풍선 하나를 만드는 시간(분) Ai를 알고 있을 때, 풍선 M개를 만들기 위해서 최소 몇 분이 걸릴까?

# 풍선을 만든 후에 문제를 표시할 것이기 때문에 풍선의 종류는 상관이 없다.

# 모든 스태프는 풍선을 만드는 데에 정확하게 자신이 말한 시간만큼 걸린다. 예를 들어 스태프 A가 풍선 하나를 만드는 데 5분이 걸린다면, 0분에 만들기 시작해서 5분에 끝난다.

# 입력
# 스태프의 수 N과 풍선의 개수 M이 입력된다. (1 ≤ N, M ≤ 1 000 000)

# 다음 줄에 N명의 각 스태프들이 풍선 하나를 만드는 데 걸리는 시간 Ai가 순서대로 주어진다. Ai는 1 000 000 이하의 자연수이다.

# 출력
# M개의 풍선이 다 만들어지는 최소 시간을 출력한다.







# 초기 코드
from collections import Counter
from sys import stdin
input = stdin.readline
n, m = map(int,input().split())
arr = Counter(map(int,input().split()))
left, right = 1, 10**12
answer = 0
while left <= right:
    mid = (left + right) // 2
    balloon = sum((mid//key)*value for key, value in arr.items())
    if balloon >= m:
        right = mid - 1
        answer = mid
    else:
        left = mid + 1
print(answer)

# 메모리, 시간, 코드길이
# 125276KB, 1976ms, 413B