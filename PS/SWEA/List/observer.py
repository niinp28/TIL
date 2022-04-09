import sys
sys.stdin = open('sample_input.txt')
T = int(input())
dx = [0, 1, 0, -1]  # 우, 하, 좌, 상
dy = [1, 0, -1, 0]
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    tot = 0  # 배열에 있는 모든 0의 갯수
    observer = 0  # 경비원이 감시 가능한 0의 갯수

    # 2차원 배열 탐색
    for r in range(N):
        for c in range(N):
            # 전체 0의 갯수 세기
            if arr[r][c] == 0:
                tot += 1

            # 경비원이 감시할 수 있는 영역 세기
            if arr[r][c] == 2:  # 경비원을 기준으로
                for d in range(4):  # 상하좌우 네 방향에 대해
                    for k in range(1, N):  # k만큼의 거리를 떨어져 있는 요소가
                        nx = r + dx[d] * k
                        ny = c + dy[d] * k
                        if 0 <= nx < N and 0 <= ny < N:  # 경계조건 만족하고
                            if arr[nx][ny] == 0:  # 0이라면
                                observer += 1  # 감시가능한 통로 변수에 1 증가
                            else:
                                break  # 경계조건을 벗어나면 바로 다음 방향으로 변경


    res = tot - observer
    print(f'#{tc} {res}')