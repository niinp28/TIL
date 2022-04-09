import sys
sys.stdin = open('maze.txt')
from collections import deque

def bfs():
    dx = [0, 1, 0, -1]  # 우 하 좌 상 의 delta
    dy = [1, 0, -1, 0]

    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r + dx[d]
            nc = c + dy[d]

            if gi == nr and gj == nc:
                arr[nr][nc] = arr[r][c] - 2
                return arr[nr][nc]
            if 0 <= nr < N and 0 <= nc < N and not(arr[nr][nc]):
                arr[nr][nc] = arr[r][c] + 1
                q.append([nr, nc])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    q = deque([])

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                q.append([i, j])
            elif arr[i][j] == 3:
                gi, gj = i, j

    res = bfs()
    if res == None:
        res = 0
    print(f'#{tc} {res}')