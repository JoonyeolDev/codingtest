# https://school.programmers.co.kr/learn/courses/30/lessons/178871
# 달리기 경주

# 문제 설명
# 얀에서는 매년 달리기 경주가 열립니다. 해설진들은 선수들이 
# 자기 바로 앞의 선수를 추월할 때 추월한 선수의 이름을 부릅니다. 

# 선수들의 이름이 1등부터 현재 등수 순서대로 담긴 문자열 배열 players와 
# 해설진이 부른 이름을 담은 문자열 배열 callings가 매개변수로 주어질 때, 
# 경주가 끝났을 때 선수들의 이름을 1등부터 등수 순서대로 배열에 담아 
# return 하는 solution 함수를 완성해주세요.

# 제한사항
# 5 ≤ players의 길이 ≤ 50,000
# players[i]는 i번째 선수의 이름을 의미합니다.
# players의 원소들은 알파벳 소문자로만 이루어져 있습니다.
# players에는 중복된 값이 들어가 있지 않습니다.
# 3 ≤ players[i]의 길이 ≤ 10
# 2 ≤ callings의 길이 ≤ 1,000,000
# callings는 players의 원소들로만 이루어져 있습니다.
# 경주 진행중 1등인 선수의 이름은 불리지 않습니다.

players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]
# ["mumu", "kai", "mine", "soe", "poe"]

# players_dict = {선수:등수}
players_dict = {}
for i, j in enumerate(players):
    players_dict[j] = i

for i in callings:
    a = players_dict[i] # 현재 순위
    cur = players[a] # 해당 순위의 선수
    pre = players[a-1] # 앞의 선수

    # players_dict에서 순위 바꾸기
    players_dict[cur] -= 1
    players_dict[pre] += 1
    
    # players 에서 위치 바꾸기
    players[a] = players[a-1]
    players[a-1] = cur
answer = players

# 제출용 함수
def solution(players, callings):
    players_dict = {}
    for i, j in enumerate(players):
        players_dict[j] = i
    for i in callings:
        a = players_dict[i] # 현재 순위
        cur = players[a] # 해당 순위의 선수
        pre = players[a-1]
        players_dict[cur] -= 1
        players_dict[pre] += 1
        players[a] = players[a-1]
        players[a-1] = cur
    answer = players
    return answer

# for i in callings:
#     a = players.index(i)
#     del players[a]
#     players.insert(a-1, i)
# answer = players

# def solution(players, callings):
#     for i in callings:
#         a = players.index(i)
#         del players[a]
#         players.insert(a-1, i)
#     answer = players
#     return answer
