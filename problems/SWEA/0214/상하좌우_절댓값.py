T = int(input())
dx = [0, 1, 0, -1]  # 우하좌상
dy = [1, 0, -1, 0]
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(5)]
    res = 0
    for r in range(5):
        for c in range(5):
            for d in range(4):
                nx = r + dx[d]
                ny = c + dy[d]
                if 0 <= nx < 5 and 0 <= ny < 5:
                    if arr[r][c] >= arr[nx][ny]:
                        res += (arr[r][c] - arr[nx][ny])
                    else:
                        res += (arr[nx][ny] - arr[r][c])

    print(f'#{tc} {res}')