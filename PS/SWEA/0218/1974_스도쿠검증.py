import sys
sys.stdin = open('1974.txt')

T = int(input())
for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    res = 0
    check1 = 0  # 3x3 배열 검사, 9가 되면 valid
    check2 = 0
    check3 = 0
    # 3x3 검사
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            check = [0] * 9
            for a in range(i, i+3):
                for b in range(j, j+3):
                    check[arr[a][b] - 1] += 1
            if check == [1] * 9:
                check1 += 1
            else:
                break

    # 가로 검사
    for r in range(9):
        r_check = [0] * 9
        for c in range(9):
            r_check[arr[r][c] - 1] += 1
        if r_check == [1] * 9:
            check2 += 1
        else:
            break

    # 세로 검사
    for c in range(9):
        c_check = [0] * 9
        for r in range(9):
            c_check[arr[r][c] - 1] += 1
        if c_check == [1] * 9:
            check3 += 1
        else:
            break
    if check1 == 9 and check2 == 9 and check3 == 9:
        res = 1
    print(f'#{tc} {res}')