# https://school.programmers.co.kr/learn/courses/30/lessons/120889
# 삼각형의 완성조건 (1)

# 문제 설명
# 선분 세 개로 삼각형을 만들기 위해서는 다음과 같은 조건을 만족해야 합니다.

# 가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야 합니다.
# 삼각형의 세 변의 길이가 담긴 배열 sides이 매개변수로 주어집니다. 
# 세 변으로 삼각형을 만들 수 있다면 1, 만들 수 없다면 2를 return하도록 
# solution 함수를 완성해주세요.

# 제한사항
# sides의 원소는 자연수입니다.
# sides의 길이는 3입니다.
# 1 ≤ sides의 원소 ≤ 1,000


sides = [1, 2, 3]

# 일단 sort로 오름차순 정리
sides.sort()

# 조건 : 가장 긴 변 < 다른 두변 합
if sides[-1] >= sides[0]+sides[1] : answer = 2
else : answer = 1

# 코드 줄이기
answer = 2 if sides[-1] >= sides[0]+sides[1] else 1

# 제출용 함수
def solution(sides):
    sides.sort()
    answer = 2 if sides[-1] >= sides[0]+sides[1] else 1
    return answer