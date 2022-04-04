import sys
sys.stdin = open('minisum.txt')
dr = [0, 1]  # 우 하
dc = [1, 0]

def dfs(r, c):
    global res, cnt
    if res and cnt >= res[-1]:
        return
    if r == N-1 and c == N-1:  # 도착점에 도달했을 때 여태 더해주었던 cnt를 저장
        res.append(cnt)
        return
    for d in range(2):
        nr = r + dr[d]
        nc = c + dc[d]
        if (0 <= nr < N) and (0 <= nc < N)\
                and (nr, nc) not in visited:
            visited.append((nr, nc))
            cnt += arr[nr][nc]
            dfs(nr, nc)
            cnt -= arr[nr][nc]  # 함수가 종료되면 원상복구
            visited.pop()  # visited 배열도 원상복구시켜서 재활용
    return res  # 모든 경로의 합들이 기록된 배열 반환

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = []
    res, cnt = [], arr[0][0]

    # 최소합 찾기
    ans = 10000
    for tmp in dfs(0, 0):
        if ans >= tmp:
            ans = tmp

    print(f'#{tc} {ans}')