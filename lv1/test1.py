# https://school.programmers.co.kr/learn/courses/30/lessons/161990
# 바탕화면 정리

# 문제 설명
# 머쓱이의 컴퓨터 바탕화면의 상태를 나타내는 
# 문자열 배열 wallpaper가 매개변수로 주어질 때 
# 바탕화면의 파일들을 한 번에 삭제하기 위해 
# 최소한의 이동거리를 갖는 드래그의 시작점과 끝점을 담은 
# 정수 배열을 return하는 solution 함수를 작성해 주세요. 
# 드래그의 시작점이 (lux, luy), 끝점이 (rdx, rdy)라면 
# 정수 배열 [lux, luy, rdx, rdy]를 return하면 됩니다.

# 제한사항
# 1 ≤ wallpaper의 길이 ≤ 50
# 1 ≤ wallpaper[i]의 길이 ≤ 50
# wallpaper의 모든 원소의 길이는 동일합니다.
# wallpaper[i][j]는 바탕화면에서 i + 1행 j + 1열에 해당하는 칸의 상태를 나타냅니다.
# wallpaper[i][j]는 "#" 또는 "."의 값만 가집니다.
# 바탕화면에는 적어도 하나의 파일이 있습니다.
# 드래그 시작점 (lux, luy)와 끝점 (rdx, rdy)는 lux < rdx, luy < rdy를 만족해야 합니다.

# 먼저 일단 예시로 주어지는 wallpaper를 출력해보자
wallpaper = [".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]

arr = []
arr2 = []
answer = []
for i in range(len(wallpaper)):
    for j in range(len(wallpaper[i])):
        # #이 있는 좌표(인덱스) 순서쌍 집합
        if wallpaper[i][j]=="#": 
            # 행만 모음
            arr.append(i)
            # 열만 모음
            arr2.append(j)

# 다음 생각할 것은 드래그를 어떻게 하느냐이다
# 쉽게 생각하면 상하좌우측 면에서 #이 처음 나오는 행과 열을 찾는다
# 이걸 이제 정리
# 상,좌,하,우 순으로 하면 된다

# 상측 면 #이 처음 나오는 라인 찾기
# arr(행)에서 젤 작은수가 처음 나오는 라인임
# sort 후 0번 인덱스 ㄱㄱ
arr.sort()
answer.append(arr[0])

# 좌측면 #이 처음 나오는 라인 찾기
# arr2(열)에서 젤 작은수가 처음 나오는 라인임
arr2.sort()
answer.append(arr2[0])

# 하측 면 #이 마지막 나오는 라인 찾기
# arr[-1]+1이 젤 마지막 나오는 하측면임
answer.append(arr[-1]+1)

# 우측면 #이 처음 나오는 라인찾기
# arr2[-1]+1이 젤 마지막 나오는 우측면임
answer.append(arr2[-1]+1)

print(answer)

# 제출용 함수로 만들기
def solution(wallpaper):
    arr = []
    arr2 = []
    answer = []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j]=="#": 
                arr.append(i)
                arr2.append(j)
    arr.sort()
    arr2.sort()
    answer.append(arr[0])
    answer.append(arr2[0])
    answer.append(arr[-1]+1)
    answer.append(arr2[-1]+1)
    return answer

