T = int(input())

for tc in range(1, T + 1):
    N, Q = map(int, input().split())
    lst = [0] * (N+1)  # 인덱스 문제를 피하기 위해 N+1 길이의 빈 리스트 생성
    for q in range(1, Q+1):  # i=1 번째 작업부터 시작이므로 range 범위를 1부터 시작
        L, R = map(int, input().split())
        for i in range(L, R+1):
            lst[i] = q

    print(f'#{tc}', *lst[1:])