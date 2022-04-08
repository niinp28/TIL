# 채워지는 면적을 표시할 2차원 배열
arr = [[0] * 100 for _ in range(100)]
# 직사각형 색칠
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    # x가 1~4일 경우, 1~2, 2~3, 3~4 세 개이므로 range에 그대로 넣어도됨.
    for x in range(x1, x2):
        for y in range(y1, y2):
            arr[x][y] += 1

cnt = 0 # 총 면적
for r in range(100):
    for c in range(100):
        if arr[r][c] > 1:  # 중복 범위를 제거하기 위해
            arr[r][c] = 1  # 1 이상이면 전부 1로 초기화 시키고
        cnt += arr[r][c]  # 카운트한다.


print(cnt)
