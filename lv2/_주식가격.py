# https://school.programmers.co.kr/learn/courses/30/lessons/42584
# 주식가격

# 문제 설명
# 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

# 제한사항
# prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
# prices의 길이는 2 이상 100,000 이하입니다.

prices = [1, 2, 3, 2, 3]
# result = [4, 3, 1, 1, 0]

# queue에 들어있는 값보다 prices의 값이 크다면 값과 인덱스, 시간 저장
# 작거나 같다면 현재 시간 - 들어간 시간을 answer 인덱스에 맞게 변경


def solution(prices):
    queue = []
    len_prices = len(prices)
    answer = [0]*len_prices
    
    for i in range(len_prices):
        while queue and prices[i] < prices[queue[-1]]:
            last_idx = queue.pop()
            answer[last_idx] = i - last_idx
        queue.append(i)
    for idx in queue:
        answer[idx] = len_prices - idx - 1
    return answer
# 28.03ms, 19.5MB


# 초기 코드
def solution(prices):
    queue = []
    len_prices = len(prices)
    answer = [False]*len_prices

    for i in range(len_prices):
        if not queue:
            queue.append((prices[i],i))
        else:
            if prices[i] > queue[-1][0]:
                queue.append((prices[i],i))
            else:
                while queue and prices[i] < queue[-1][0]:
                    _, last_idx = queue.pop()
                    answer[last_idx] = i - last_idx
                queue.append((prices[i],i))
    for _, idx in queue:
        answer[idx] = len_prices-idx-1
    return answer
# 38.51ms, 19.4MB
