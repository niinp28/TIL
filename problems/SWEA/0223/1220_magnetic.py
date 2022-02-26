import sys; sys.stdin = open('1220.txt')

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    ans = 0  # 교착 상태 수
    for c in range(100):
        # 열탐색을 시작하기 전에 상태를 초기화
        state = 0       # 0: 1을 만나기 전, 1: 1을 만난 후
        for r in range(100):
            if state == 0 and arr[r][c] == 1:
                state = 1
            if state == 1 and arr[r][c] == 2:
                ans += 1
                state = 0
    print(ans)