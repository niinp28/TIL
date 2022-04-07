import sys
sys.stdin = open('미로찾기.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    stack = []
    visited = []
    res = 0
    # 출발점 탐색
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 2:
                stack.append((r, c))

    while stack:
        cr, cc = stack.pop()
        visited.append((cr, cc))
        for dr, dc in (0, 1), (1, 0), (0, -1), (-1, 0):
            nr = cr + dr
            nc = cc + dc
            if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in visited:
                if arr[nr][nc] == 0:
                    stack.append((nr, nc))
                elif arr[nr][nc] == 1:
                    continue
                elif arr[nr][nc] == 3:
                    res = 1
                    break
    print(f'#{tc} {res}')