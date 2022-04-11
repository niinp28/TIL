import sys
sys.stdin = open('연산.txt')
from collections import deque
def solution(start, goal):
    q = deque()
    q.append((start, 0))
    used = {}
    while q:
        num, cnt = q.popleft()
        if used.get(num, 0):  # 이미 사용한 숫자가 존재하면 할 필요가 없다(pruning)
            continue
        used[num] = True
        if num == goal:  # 목표 숫자에 도달한다면 리턴
            return cnt
        cnt += 1
        # 4가지 연산을 현재 상태에서 모두 해보며 결과를 도출한다.
        if 0 < num + 1 <= 1e6: # 연산을 해도 자연수 조건과 100만 이하를 만족해야함. 이하 동일
            q.append((num+1, cnt))
        if 0 < num - 1 <= 1e6:
            q.append((num-1, cnt))
        if 0 < num * 2 <= 1e6:
            q.append((num*2, cnt))
        if 0 < num - 1 <= 1e6:
            q.append((num-10, cnt))
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    res = solution(N, M)
    print(f'#{tc} {res}')
