T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    road = [0] * 200  # 경로를 표시할 리스트
    # 각 학생들의 경로가 겹치는 만큼의 단위시간이 걸리게 된다.
    # 시작점과 끝점을 설정하고 양 끝점과 그 사이의 경로에 대해 road리스트에서 1을 더해준다
    # 최종 리스트에서 가장 큰 숫자만큼 단위 시간이 걸리게 되므로 이를 구한다.
    for student in lst:
        if student[0] < student[-1]:
            s = (student[0] - 1) // 2
            e = (student[-1] - 1) // 2
        else:
            s = (student[-1] - 1) // 2
            e = (student[0] - 1) // 2
        for i in range(s, e+1):
            road[i] += 1
    mx = 0
    for num in road:
        if mx < num:
            mx = num
    print(f'#{tc} {mx}')