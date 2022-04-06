import sys
sys.stdin = open('N-queen.txt')
def dfs(n):
    global res
    if n == N:
        res += 1
        return

    for j in range(N):
        if col[j] == vru[n + j] == vrd[n - j] == 0:
            col[j] = vru[n + j] = vrd[n - j] = 1
            dfs(n + 1)
            col[j] = vru[n + j] = vrd[n - j] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    res = 0
    # 열, ↗, ↘
    col, vru, vrd = [0] * N, [0] * (2*N - 1), [0] * (2*N - 1)
    dfs(0)
    print(f'#{tc} {res}')