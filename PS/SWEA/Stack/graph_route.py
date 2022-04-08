import sys
sys.stdin = open('graph_route.txt')
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = {}
    for _ in range(E):
        a, z = map(int, input().split())
        graph[a] = graph.get(a, []) + [z]
    S, G = map(int, input().split())
    res = 0
    stack = [S]
    visited = []
    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            if n in graph.keys():
                for m in graph[n]:
                    stack.append(m)
    if G in visited:
        res = 1
    print(f'#{tc} {res}')


