T = int(input())

for tc in range(1, T + 1):
    lst = input()
    res = cnt = 0
    for i in range(len(lst)):
        if lst[i] == '(':  # 막대기 추가
            cnt += 1
        else:
            if lst[i-1] == '(':  # 레이저
                cnt -= 1  # 막대기가 아니었으므로 하나 감소
                res += cnt  # 레이저로 인해 막대 조각이 생성되었으므로 cnt 만큼 증가
            else:  # 막대기 제거
                cnt -= 1
                res += 1
    print(f'#{tc} {res}')