# https://www.acmicpc.net/problem/1107
# 리모컨

# 문제
# 수빈이는 TV를 보고 있다. 수빈이는 채널을 돌리려고 했지만, 버튼을 너무 세게 누르는 바람에, 일부 숫자 버튼이 고장났다.
# 리모컨에는 버튼이 0부터 9까지 숫자, +와 -가 있다. +를 누르면 현재 보고있는 채널에서 +1된 채널로 이동하고, -를 누르면 -1된 채널로 이동한다. 채널 0에서 -를 누른 경우에는 채널이 변하지 않고, 채널은 무한대 만큼 있다.
# 수빈이가 지금 이동하려고 하는 채널은 N이다. 어떤 버튼이 고장났는지 주어졌을 때, 채널 N으로 이동하기 위해서 버튼을 최소 몇 번 눌러야하는지 구하는 프로그램을 작성하시오.
# 수빈이가 지금 보고 있는 채널은 100번이다.

# 입력
# 첫째 줄에 수빈이가 이동하려고 하는 채널 N (0 ≤ N ≤ 500,000)이 주어진다. 둘째 줄에는 고장난 버튼의 개수 M (0 ≤ M ≤ 10)이 주어진다. 고장난 버튼이 있는 경우에는 셋째 줄에는 고장난 버튼이 주어지며, 같은 버튼이 여러 번 주어지는 경우는 없다.

# 출력
# 첫째 줄에 채널 N으로 이동하기 위해 버튼을 최소 몇 번 눌러야 하는지를 출력한다.

from itertools import product
from sys import stdin
input = stdin.readline

n = int(input())
m = int(input())


# 초기 코드 : 틀림
def remote_controller(n, m):
    len_n = len(str(n))
    if not m:
        return min(abs(n-100),len_n)
    broken_buttons = list(map(int, input().split()))
    if n == 100:
        return 0
    elif m == 10:
        return abs(n-100)
    buttons = [str(num) for num in range(10) if num not in broken_buttons]
    min_gap = abs(n-100)
    for pro in product(buttons, repeat=len_n):
        num = int(''.join(pro))
        min_gap = min(abs(n-num)+len_n, min_gap)
    if not (m == 9 and buttons[0]=='0'):
        if buttons[0] == '0':
            max_num = buttons[1]+'0'*(len_n)
        else:
            max_num = buttons[0]*(len_n+1)
            print(buttons[0])
        max_num_gap = abs(n-int(max_num))+len_n+1
        min_num_gap = abs(n-int(buttons[-1]*(len_n-1)))+len_n-1
        min_gap = min(min_num_gap, min_gap, max_num_gap)
    else:
        min_gap = min(n+1, abs(n-100))
    return min_gap

print(remote_controller(n, m))