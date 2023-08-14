# https://school.programmers.co.kr/learn/courses/30/lessons/68644
# 두 개 뽑아서 더하기

# 문제 설명
# 정수 배열 numbers가 주어집니다. numbers에서 서로 다른 인덱스에 있는 
# 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 
# return 하도록 solution 함수를 완성해주세요.

# 제한사항
# numbers의 길이는 2 이상 100 이하입니다.
# numbers의 모든 수는 0 이상 100 이하입니다.

numbers = [2,1,3,4,1]

answer = []
# 이것도 combinations 쓰면 쉬움
# 근데 임포트하기 귀찮으니깐 그냥 for문으로 작성
for i in range(len(numbers)-1):
    for j in range(i+1,len(numbers)):
        answer.append(numbers[i]+numbers[j])
# 중복 제거 후 정렬
answer = list(set(answer))
answer.sort()
print(answer)