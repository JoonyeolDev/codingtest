# https://school.programmers.co.kr/learn/courses/30/lessons/77484
# 로또의 최고 순위와 최저 순위

# 민우가 구매한 로또 번호를 담은 배열 lottos, 당첨 번호를 담은 배열 win_nums가 
# 매개변수로 주어집니다. 이때, 당첨 가능한 최고 순위와 최저 순위를 
# 차례대로 배열에 담아서 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# lottos는 길이 6인 정수 배열입니다.
# lottos의 모든 원소는 0 이상 45 이하인 정수입니다.
# 0은 알아볼 수 없는 숫자를 의미합니다.
# 0을 제외한 다른 숫자들은 lottos에 2개 이상 담겨있지 않습니다.
# lottos의 원소들은 정렬되어 있지 않을 수도 있습니다.
# win_nums은 길이 6인 정수 배열입니다.
# win_nums의 모든 원소는 1 이상 45 이하인 정수입니다.
# win_nums에는 같은 숫자가 2개 이상 담겨있지 않습니다.
# win_nums의 원소들은 정렬되어 있지 않을 수도 있습니다.

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
# result = [3, 5]

# 로도 당첨 경우의 수 dic으로
dic = {"0":6,"1":6,"2":5,"3":4,"4":3,"5":2,"6":1}
count = 0
zero_count = 0
for i in lottos:
    if i in win_nums: count+=1
    elif i==0: zero_count+=1
answer = [dic[str(count+zero_count)],dic[str(count)]]
print(answer)

# 제출용 함수
def solution(lottos, win_nums):
    dic = {"0":6,"1":6,"2":5,"3":4,"4":3,"5":2,"6":1}
    count = 0
    zero_count = 0
    for i in lottos:
        if i in win_nums: count+=1
        elif i==0: zero_count+=1
    answer = [dic[str(count+zero_count)],dic[str(count)]]
    return answer