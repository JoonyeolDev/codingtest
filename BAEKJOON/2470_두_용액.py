# https://www.acmicpc.net/problem/2470
# 용액

# 문제
# KOI 부설 과학연구소에서는 많은 종류의 산성 용액과 알칼리성 용액을 보유하고 있다. 각 용액에는 그 용액의 특성을 나타내는 하나의 정수가 주어져있다. 산성 용액의 특성값은 1부터 1,000,000,000까지의 양의 정수로 나타내고, 알칼리성 용액의 특성값은 -1부터 -1,000,000,000까지의 음의 정수로 나타낸다.
# 같은 양의 두 용액을 혼합한 용액의 특성값은 혼합에 사용된 각 용액의 특성값의 합으로 정의한다. 이 연구소에서는 같은 양의 두 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들려고 한다. 
# 예를 들어, 주어진 용액들의 특성값이 [-99, -2, -1, 4, 98]인 경우에는 특성값이 -99인 용액과 특성값이 98인 용액을 혼합하면 특성값이 -1인 용액을 만들 수 있고, 이 용액의 특성값이 0에 가장 가까운 용액이다. 참고로, 두 종류의 알칼리성 용액만으로나 혹은 두 종류의 산성 용액만으로 특성값이 0에 가장 가까운 혼합 용액을 만드는 경우도 존재할 수 있다.
# 산성 용액과 알칼리성 용액의 특성값이 정렬된 순서로 주어졌을 때, 이 중 두 개의 서로 다른 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들어내는 두 용액을 찾는 프로그램을 작성하시오.

# 입력
# 첫째 줄에는 전체 용액의 수 N이 입력된다. N은 2 이상 100,000 이하의 정수이다. 둘째 줄에는 용액의 특성값을 나타내는 N개의 정수가 빈칸을 사이에 두고 오름차순으로 입력되며, 이 수들은 모두 -1,000,000,000 이상 1,000,000,000 이하이다. N개의 용액들의 특성값은 모두 서로 다르고, 산성 용액만으로나 알칼리성 용액만으로 입력이 주어지는 경우도 있을 수 있다.

# 출력
# 첫째 줄에 특성값이 0에 가장 가까운 용액을 만들어내는 두 용액의 특성값을 출력한다. 출력해야 하는 두 용액은 특성값의 오름차순으로 출력한다. 특성값이 0에 가장 가까운 용액을 만들어내는 경우가 두 개 이상일 경우에는 그 중 아무것이나 하나를 출력한다.

n = 5
arr = [-99, -2, -1, 4, 98]

n = 4
arr = [-100, -2, -1, 103]


# 1차 수정 : 투 포인터
from sys import stdin
input = stdin.readline
n = int(input().rstrip('\n'))
arr = list(map(int, input().split()))
left = 0
right = n-1
min_value = (abs(arr[0] + arr[-1]), 0, -1)
while left + 1 < right:
    value = arr[left] + arr[right]
    if not value:
        print(f'{arr[left]} {arr[right]}')
        break
    elif value > 0:
        right -= 1
    else:
        left += 1
    if min_value[0] > abs(arr[left] + arr[right]):
        min_value = (abs(arr[left] + arr[right]), left, right)
else:
    print(f'{arr[min_value[1]]} {arr[min_value[2]]}')
# 42176KB, 148ms, 551B



# 초기 코드 : 시간초과
n = 5
arr = [-99, -2, -1, 4, 98]
def solution(n, arr):
    min_sum = (arr[-1] + arr[-2],-1,-2)
    for i in range(n - 1):
        for j in range(i+1, n):
            sum_ = abs(arr[i]+arr[j])
            if not sum_:
                return f'{arr[i]} {arr[j]}'
            elif sum_ < min_sum[0]:
                min_sum = (sum_, i, j)
    return f'{arr[min_sum[1]]} {arr[min_sum[2]]}'
# print(solution(n, arr))