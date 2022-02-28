import sys
sys.stdin = open('search_route.txt')
for _ in range(10):
    tc, n = map(int, input().split())
    lst = list(map(int, input().split()))
    graph = {}
    # 딕셔너리로 경로에 대한 정보를 저장
    for i in range(0, n*2, 2):
        k = lst[i]
        v = lst[i+1]
        graph[lst[i]] = graph.get(k, []) + [lst[i+1]]

    stack = [0]  # 시작 지점이 0이므로 0을 추가
    visited = [0] * 100
    while stack:
        a = stack.pop()
        if visited[a] == 0:
            visited[a] = 1
        if a in graph.keys():
            for j in graph[a]:
                if visited[j] == 0:
                    stack.append(j)
    if visited[-1] == 1:
        res = 1
    else:
        res = 0
    print(f'#{tc} {res}')