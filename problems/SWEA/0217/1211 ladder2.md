# 1211. Ladder2

```python
dx = [0, 1, 0]  # 좌, 하, 우
dy = [-1, 0, 1]
for _ in range(10):
    tc = int(input())
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]  # index 문제를 피하기 위해 양쪽에 벽을 세움
    min_dict = {}  # 각 출발점과 도착적을 매칭시킬 빈 딕셔너리 생성
    d = 1  # 기본 방향 :  하
    for j in range(102):
        cnt = 0  # 출발점 마다 변수를 전부 초기화
        tmp = 0
        x, y = 0, 0
        if arr[0][j] == 1:  # 출발점을 찾으면
            y = j  # y를 j로 할당해주고
            tmp = j  # tmp에 시작점을 표시해둔다

            while True:
                if x == 99:  # 끝에 오면 break
                    cnt += 1
                    break
                # 오른쪽 로직
                if arr[x][y+1] == 1:  # 오른쪽에 1이 써져 있으면
                    while 1:  # cnt를 증가, 방향을 오른쪽으로 설정하고 x, y를 dx, dy만큼 증가
                        cnt += 1
                        d = 2
                        x += dx[d]
                        y += dy[d]
                        if arr[x][y+1] == 0:  # 만약 오른쪽이 0이라면 방향을 아래로 초기화 하고 break
                            d = 1
                            break
                # 왼쪽 로직
                elif arr[x][y-1] == 1:
                    while 1:
                        cnt += 1
                        d = 0
                        x += dx[d]
                        y += dy[d]
                        if arr[x][y-1] == 0:
                            cnt += 1
                            d = 1
                            break
                # 내려가기
                cnt += 1
                x += dx[d]
                y += dy[d]
            min_dict[tmp-1] = cnt  # 벽을 세웠으므로 tmp에 1을 뺀 값이 원래의 인덱스이다. 딕셔너리에 (시작점: 횟수)를 기입

    mn = 10000  # value들보다 작아지지 않도록 임의의 큰 값을 설정
    res = 0
    for k, v in min_dict.items():  # 최소 횟수를 먼저 할당
        if mn >= v:
            mn = v

    for k, v in min_dict.items():  # 최소 횟수에 해당하는 k를 뽑아 res에 할당한다.
        if v == mn:
            res = k
    print(f'#{tc} {res}')
```

