T = 10
for _ in range(1, T+1):
    tc = int(input())
    q = list(map(int, input().split()))

    i = 1
    while 1:
        if i > 5:  # 감소량이 5보다 커지면 1로 초기화한다.
            i = 1
        t = q.pop(0) - i  # 첫번째 요소를 i만큼 감소시키고 꺼낸다.
        if t <= 0:  # 만약 감소시키고 난 뒤 0보다 작으면 0을 붙이고 종료한다.
            q.append(0)
            break
        q.append(t)  # 큐의 맨 뒤에다가 넣는다
        i += 1

    print(f'#{tc} {q[0]} {q[1]} {q[2]} {q[3]} {q[4]} {q[5]} {q[6]} {q[7]}')