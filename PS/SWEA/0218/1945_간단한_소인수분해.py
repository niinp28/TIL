import sys
sys.stdin = open('soinsu.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = [2, 3, 5, 7, 11, 0]
    d = {2: 0, 3: 0, 5: 0, 7: 0, 11: 0}
    n = lst[0]
    i = 0
    while i < 5:
        if N % n == 0:
            N //= n
            d[n] += 1
        else:
            i += 1
            n = lst[i]
    print(f'#{tc} {d[2]} {d[3]} {d[5]} {d[7]} {d[11]}')