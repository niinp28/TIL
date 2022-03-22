import sys
sys.stdin = open('paper.txt')
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    dp = []
    for num in range(N//10):
        if num == 0:  # specific case 는 직접 값을 넣어준다
            dp.append(1)
        elif num == 1:  # 위와 동일
            dp.append(3)
        # 전 단계에서 20x10 붙이는 방식은 한가지
        # 전전 단계에서 20x20 한개, 20x10을 가로로 2개 붙이는 방식
        # 총 두 가지가 발생한다.
        else:
            dp.append(dp[num - 1] + 2 * dp[num - 2])

    print(f'#{tc} {dp[-1]}')