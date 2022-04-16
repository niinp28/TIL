import sys
sys.stdin = open('cargo_dock.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    newlst = sorted(lst, key=lambda x: x[1])  # 종료 지점 기준으로 sorting
    cnt = 0  # 화물차 수
    time = 0  # 현재 시간
    for truck in newlst:
        if time <= truck[0]:  # 현재 시간은 새로 출발할 시간보다 앞이어야 한다.
            time = truck[1]  # 종료 시점을 새로운 현재 시간으로 할당
            cnt += 1

    print(f'#{tc} {cnt}')
