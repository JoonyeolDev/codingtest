# https://school.programmers.co.kr/learn/courses/30/lessons/42842

# 문제 설명
# Leo는 카펫을 사러 갔다가 아래 그림과 같이 중앙에는 노란색으로 칠해져 있고 테두리 1줄은 갈색으로 칠해져 있는 격자 모양 카펫을 봤습니다.

# Leo는 집으로 돌아와서 아까 본 카펫의 노란색과 갈색으로 색칠된 격자의 개수는 기억했지만, 전체 카펫의 크기는 기억하지 못했습니다.

# Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 갈색 격자의 수 brown은 8 이상 5,000 이하인 자연수입니다.
# 노란색 격자의 수 yellow는 1 이상 2,000,000 이하인 자연수입니다.
# 카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다.

brown, yellow = 10, 2
# return = [4, 3]

# 주어진 brown과 yellow를 사용해 가로/ 세로를 구할 수 있음
# 가로 * 세로 = brown + yellow 를 사용하면 될 듯
# 조건에 가로 길이는 세로 길이와 같거나 길다고 하니 넓이의 제곱근부터 시작하면 될 듯


# 1차 수정 : 가독성 개선 및 조건 정리
def solution(brown, yellow):
    total_area = brown + yellow
    sqrt_total_area = int(total_area**(0.5))
    if sqrt_total_area * 2 - 4 == brown:
        return [sqrt_total_area, sqrt_total_area]
    for height in range(3, sqrt_total_area + 1):
        if total_area % height == 0:
            width = total_area // height
            if (width + height) * 2 - 4 == brown:
                return [width, height]
# 0.15ms


# 초기 코드
def solution(brown, yellow):
    sum_width_height = brown // 2 + 2
    sum_brown_yellow = brown + yellow
    for width in range(int(sum_brown_yellow**(0.5)),sum_width_height):
        height = sum_width_height - width
        if width * height == sum_brown_yellow and width >= height:
            return [width, height]
# 0.25ms

print(solution(brown, yellow))