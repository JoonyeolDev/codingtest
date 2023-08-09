# https://school.programmers.co.kr/learn/courses/30/lessons/42583

# 문제 설명
# 트럭 여러 대가 강을 가로지르는 일차선 다리를 정해진 순으로 건너려 합니다. 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다. 다리에는 트럭이 최대 bridge_length대 올라갈 수 있으며, 다리는 weight 이하까지의 무게를 견딜 수 있습니다. 단, 다리에 완전히 오르지 않은 트럭의 무게는 무시합니다.
# solution 함수의 매개변수로 다리에 올라갈 수 있는 트럭 수 bridge_length, 다리가 견딜 수 있는 무게 weight, 트럭 별 무게 truck_weights가 주어집니다. 이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return 하도록 solution 함수를 완성하세요.

# 제한 조건
# bridge_length는 1 이상 10,000 이하입니다.
# weight는 1 이상 10,000 이하입니다.
# truck_weights의 길이는 1 이상 10,000 이하입니다.
# 모든 트럭의 무게는 1 이상 weight 이하입니다.

bridge_length, weight, truck_weights = 2, 10, [7,4,5,6]
# result = 8


# 3차 수정, 2489.66 ms > 0.31ms
# 다리 체크 > 트럭과 조건 체크 > 트럭 들어간 시간 체크
# 불필요한 while 반복을 줄임
from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque()
    sum_weight = 0
    trucks = deque(truck_weights)
    while trucks or bridge:
        if bridge and bridge[0][1] == answer:
            exiting_truck, _ = bridge.popleft()
            sum_weight -= exiting_truck
        if trucks and sum_weight + trucks[0] <= weight:
            current_truck = trucks.popleft()
            bridge.append((current_truck, answer + bridge_length))
            sum_weight += current_truck
        else:
            if bridge:
                answer = bridge[0][1] - 1
        answer += 1
    return answer

print(solution(bridge_length, weight, truck_weights))



# 초기 코드 : list, insert, pop
def solution(bridge_length, weight, truck_weights):
    answer=0
    bridge = [0]*bridge_length
    idx = 0
    count=0
    sum_weight = 0
    while len(truck_weights)>count:
        answer+=1
        try:
            if weight >= (sum_weight+truck_weights[idx]-bridge[-1]):
                bridge.insert(0,truck_weights[idx])
                sum_weight+=truck_weights[idx]
                idx+=1
            else:
                bridge.insert(0,0)
        except:
            bridge.insert(0,0)
        if len(bridge)>=bridge_length:
            a = bridge.pop()
            if a in truck_weights:
                count+=1
                sum_weight-=a
    return answer
# 3122.41ms


# 1차 수정 : 자료형 변경 deque, appendleft, pop
from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer=0
    bridge = deque([0]*bridge_length)
    idx = 0
    count=0
    sum_weight = 0
    while len(truck_weights)>count:
        answer+=1
        try:
            if weight >= (sum_weight+truck_weights[idx]-bridge[-1]):
                bridge.appendleft(truck_weights[idx])
                sum_weight+=truck_weights[idx]
                idx+=1
            else:
                bridge.appendleft(0)
        except:
            bridge.appendleft(0)
        if len(bridge)>=bridge_length:
            a = bridge.pop()
            if a in truck_weights:
                count+=1
                sum_weight-=a
    return answer
# 2489.66ms


# 2차 수정 : 불필요한 로직 삭제/변경
from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length)
    sum_weight = 0
    trucks = deque(truck_weights)
    
    while trucks or sum_weight > 0:
        answer += 1
        sum_weight -= bridge.pop()
        
        if trucks and sum_weight + trucks[0] <= weight:
            current_truck = trucks.popleft()
            bridge.appendleft(current_truck)
            sum_weight += current_truck
        else:
            bridge.appendleft(0)
    return answer
# 68.56ms