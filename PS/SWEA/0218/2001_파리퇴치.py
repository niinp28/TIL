T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    lst = []
    for i in range(N - M + 1):
        for j in range(N - M + 1):  # 파리채가 들어갈 수 있는 모든 공간 탐색
            cnt = 0
            for a in range(i, i + M):  # 파리채에 죽은 파리들의 수를 저장
                for b in range(j, j + M):
                    cnt += arr[a][b]
            lst.append(cnt)
    mx = lst[0]
    for num in lst:  # 파리의 수를 담은 리스트에서 최댓값 구하기
        if mx <= num:
            mx = num

    print(f'#{tc} {mx}')
