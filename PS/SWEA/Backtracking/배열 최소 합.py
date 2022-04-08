import sys
sys.stdin = open('배열 최소합.txt')
def dfs(idx, total):
    global res
    if idx == N:
        if res > total:
            res = total
        return
    elif res < total:
        return
    else:
        for c in range(N):
            if not visited[c]:
                visited[c] = 1
                dfs(idx+1, total+arr[idx][c])
                visited[c] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    res = 1e9
    dfs(0, 0)
    print(f'#{tc} {res}')