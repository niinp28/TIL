import sys
sys.stdin = open('기지국_in.txt')
dx = [0, 1, 0, -1]  # 우, 하, 좌, 상
dy = [1, 0, -1, 0]
for _ in range(2):

    N = int(input())
    arr = [list(input()) for _ in range(N)]
    cnt = 0

    for r in range(N):
        for c in range(N):
            if arr[r][c] == 'A':
                for d in range(4):
                    nx = r + dx[d]
                    ny = c + dy[d]
                    if 0 <= nx < 9 and 0 <= ny < 9:
                        if arr[nx][ny] == 'H':
                            arr[nx][ny] = 'X'
            elif arr[r][c] == 'B':
                for d in range(4):
                    for a in range(1, 3):
                        nx = r + dx[d] * a
                        ny = c + dy[d] * a
                        if 0 <= nx < 9 and 0 <= ny < 9:
                            if arr[nx][ny] == 'H':
                                arr[nx][ny] = 'X'
            elif arr[r][c] == 'C':
                for d in range(4):
                    for a in range(1, 4):
                        nx = r + dx[d] * a
                        ny = c + dy[d] * a
                        if 0 <= nx < 9 and 0 <= ny < 9:
                            if arr[nx][ny] == 'H':
                                arr[nx][ny] = 'X'

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'H':
                cnt += 1

    print(cnt)