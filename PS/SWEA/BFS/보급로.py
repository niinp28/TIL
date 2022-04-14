import sys
sys.stdin = open('보급로.txt')
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
def bfs(er, ec):
    q = [(0, 0)]
    v[0][0] = arr[0][0]
    while q:
        r, c = q.pop(0)
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and v[nr][nc] > v[r][c] + arr[nr][nc]:
                q.append((nr, nc))
                v[nr][nc] = v[r][c] + arr[nr][nc]
    return v[er][ec]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    v = [[float('inf')] * N for _ in range(N)]
    res = bfs(N-1, N-1)
    print(f'#{tc} {res}')