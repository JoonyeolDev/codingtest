# https://www.acmicpc.net/problem/9019
# DSLR

# 문제
# 네 개의 명령어 D, S, L, R 을 이용하는 간단한 계산기가 있다. 이 계산기에는 레지스터가 하나 있는데, 이 레지스터에는 0 이상 10,000 미만의 십진수를 저장할 수 있다. 각 명령어는 이 레지스터에 저장된 n을 다음과 같이 변환한다. n의 네 자릿수를 d1, d2, d3, d4라고 하자(즉 n = ((d1 × 10 + d2) × 10 + d3) × 10 + d4라고 하자)

# D: D 는 n을 두 배로 바꾼다. 결과 값이 9999 보다 큰 경우에는 10000 으로 나눈 나머지를 취한다. 그 결과 값(2n mod 10000)을 레지스터에 저장한다.
# S: S 는 n에서 1 을 뺀 결과 n-1을 레지스터에 저장한다. n이 0 이라면 9999 가 대신 레지스터에 저장된다.
# L: L 은 n의 각 자릿수를 왼편으로 회전시켜 그 결과를 레지스터에 저장한다. 이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d2, d3, d4, d1이 된다.
# R: R 은 n의 각 자릿수를 오른편으로 회전시켜 그 결과를 레지스터에 저장한다. 이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d4, d1, d2, d3이 된다.
# 위에서 언급한 것처럼, L 과 R 명령어는 십진 자릿수를 가정하고 연산을 수행한다. 예를 들어서 n = 1234 라면 여기에 L 을 적용하면 2341 이 되고 R 을 적용하면 4123 이 된다.
# 여러분이 작성할 프로그램은 주어진 서로 다른 두 정수 A와 B(A ≠ B)에 대하여 A를 B로 바꾸는 최소한의 명령어를 생성하는 프로그램이다. 예를 들어서 A = 1234, B = 3412 라면 다음과 같이 두 개의 명령어를 적용하면 A를 B로 변환할 수 있다.
# 1234 →L 2341 →L 3412
# 1234 →R 4123 →R 3412
# 따라서 여러분의 프로그램은 이 경우에 LL 이나 RR 을 출력해야 한다.
# n의 자릿수로 0 이 포함된 경우에 주의해야 한다. 예를 들어서 1000 에 L 을 적용하면 0001 이 되므로 결과는 1 이 된다. 그러나 R 을 적용하면 0100 이 되므로 결과는 100 이 된다.

# 입력
# 프로그램 입력은 T 개의 테스트 케이스로 구성된다. 테스트 케이스 개수 T 는 입력의 첫 줄에 주어진다. 각 테스트 케이스로는 두 개의 정수 A와 B(A ≠ B)가 공백으로 분리되어 차례로 주어지는데 A는 레지스터의 초기 값을 나타내고 B는 최종 값을 나타낸다. A 와 B는 모두 0 이상 10,000 미만이다.

# 출력
# A에서 B로 변환하기 위해 필요한 최소한의 명령어 나열을 출력한다. 가능한 명령어 나열이 여러가지면, 아무거나 출력한다.


# 2차 수정 : 자료형 수정, 로직 수정
from collections import deque
from sys import stdin
input = stdin.readline

orders = ["D", "S", "L", "R"]
for _ in range(int(input())):
    a, b = map(int, input().split())
    q = deque([a])
    q_od = deque([0])
    visited = [0] * 10000

    while q:
        num = q.popleft()
        order = q_od.popleft()
        if num == b:
            print(''.join(orders[int(i)-1] for i in str(order)))
            break
        commands = [
            num * 2 % 10000,
            9999 if num == 0 else num - 1,
            num * 10 % 10000 + num // 1000,
            num // 10 + num % 10 * 1000
        ]
        for command, next_num in enumerate(commands, 1):
            if not visited[next_num]:
                q.append(next_num)
                q_od.append(order * 10 + command)
                visited[next_num] = 1
# pypy3, 212468KB, 5820ms, 819B


# 1차 수정 : 로직 수정
from collections import deque
from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    a, b = map(int, input().split())
    queue = deque([(a, "")])
    visited = [0] * 10000

    while queue:
        num, order = queue.popleft()
        if num == b:
            print(order)
            break
        str_num = str(num).rjust(4, '0')
        commands = {
            "D": num * 2 % 10000,
            "S": 9999 if num == 0 else num - 1,
            "L": int(str_num[1:] + str_num[0]),
            "R": int(str_num[-1] + str_num[:-1])
        }
        for command, next_num in commands.items():
            if not visited[next_num]:
                queue.append((next_num, order + command))
                visited[next_num] = 1
# pypy3, 215092KB, 11900ms, 752B


# 초기 코드 : 시간초과
from collections import deque
from sys import stdin
input = stdin.readline

def register(num, command):
    num = "0" * (4 - len(num)) + num
    if command == "D":
        num = str(int(num) * 2 % 10000)
    elif command == "S":
        num = str(int(num) - 1) if int(num) > 0 else "9999"
    elif command == "L":
        num = num[1:] + num[0]
    else:
        num = num[3] + num[:3]
    num = "0" * (4 - len(num)) + num
    return num

commands = ["D", "S", "L", "R"]

for _ in range(int(input())):
    a, b = input().split()
    queue = deque([(a, "")])
    visited = set([a])

    while queue:
        num, order = queue.popleft()
        if int(num) == int(b):
            break
        for command in commands:
            next_num = register(num, command)
            if next_num not in visited:
                queue.append((next_num, order + command))
                visited.add(next_num)
    print(order)