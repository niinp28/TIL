T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    length = 0
    # 가로
    for i in range(N):
        cnt = 0
        mx = 0
        for j in range(N):
            if j < N-1:
                if arr[i][j] == 1 and arr[i][j+1] == 1:
                    cnt += 1
                else:
                    if mx < cnt + 1:
                        mx = cnt + 1
                    cnt = 0
        if mx == K:
            length += 1

    # 세로
    for j in range(N):
        cnt = 0
        mx = 0
        for i in range(N):
            if i < N-1:
                if arr[i][j] == 1 and arr[i+1][j] == 1:
                    cnt += 1
                else:
                    if mx < cnt + 1:
                        mx = cnt + 1
                    cnt = 0
        if mx == K:
            length += 1

    print(f'#{tc} {length}')
