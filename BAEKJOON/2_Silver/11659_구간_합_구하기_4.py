# https://www.acmicpc.net/problem/11659
# 구간 합 구하기 4

# 문제
# 수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M이 주어진다. 둘째 줄에는 N개의 수가 주어진다. 수는 1,000보다 작거나 같은 자연수이다. 셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j가 주어진다.

# 출력
# 총 M개의 줄에 입력으로 주어진 i번째 수부터 j번째 수까지 합을 출력한다.


# 1차 수정
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
sum_ = 0
sum_dict = {0:0}
for i, num in enumerate(arr, 1):
    sum_ += num
    sum_dict[i] = sum_
for _ in range(m):
    i, j = map(int, input().split())
    print(sum_dict[j]-sum_dict[i-1])
# 48780KB, 280ms, 299B


# 초기 코드
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
sum_ = 0
min_num = 100000
max_num = 1
arr_ij = []
for _ in range(m):
    i, j = map(int, input().split())
    min_num = min(min_num, i)
    max_num = max(max_num, j)
    arr_ij.append((i, j))
sum_dict = {min_num-1:0}
for i, num in enumerate(arr[min_num-1:max_num+1], min_num):
    sum_ += num
    sum_dict[i] = sum_
for i, j in arr_ij:
    print(sum_dict[j]-sum_dict[i-1])

# 62632KB, 376ms, 481B