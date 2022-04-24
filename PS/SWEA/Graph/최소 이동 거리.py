import sys
sys.stdin = open('최소 이동 거리.txt')

T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    arr = [[0] * (N+1) for _ in range(N+1)]
    dis = [float('inf')] * (N+1)
    dis[0] = 0
    # 입력받기
    for i in range(E):
        s, e, w = map(int, input().split())
        arr[s][e] = w

    for r in range(N+1):
        for c in range(N+1):  # c, 즉 열은 목적지의 의미를 담고 있다
            if arr[r][c] != 0 and dis[c] > arr[r][c] + dis[r]:
                dis[c] = arr[r][c] + dis[r]
    print(f'#{tc} {dis[N]}')