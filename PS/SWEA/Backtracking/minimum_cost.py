import sys
sys.stdin = open('minimum_cost.txt')
def DFS(idx, total):  # idx : 행의 인덱스, total : 총합
    global res
    if total >= res:  # pruning
        return
    if idx == N:
        res = total
    for i in range(N):
        if not visited[i]:
            visited[i] = 1  # 방문하지 않은 곳이면 1로 방문 처리
            DFS(idx+1, total+arr[idx][i])  # 다음 행에서 진행, total은 현재 칸의 값을 더해서 보냄
            visited[i] = 0  # 원상복구

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    res = 1e9
    DFS(0, 0)
    print(f'#{tc} {res}')