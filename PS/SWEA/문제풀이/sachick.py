import sys
sys.stdin = open('sachick.txt')

for tc in range(1, 11):
    N = int(input())
    lst = list(input().split() for _ in range(N))
    tree = [0] * (N+1)
    child = {}
    for l in lst:
        tree[int(l[0])] = l[1]
        if l[2:]:
            child[int(l[0])] = [int(l[2])]
            if l[3:]:
                child[int(l[0])] = child.get(int(l[0])) + [int(l[3])]
    print(tree)
    for node in range(len(tree)-1, 0, -1):
        if tree[node] == '-':
            tree[node] = int(tree[child[node][0]]) - int(tree[child[node][1]])
        elif tree[node] == '+':
            tree[node] = int(tree[child[node][0]]) + int(tree[child[node][1]])
        elif tree[node] == '*':
            tree[node] = int(tree[child[node][0]]) * int(tree[child[node][1]])
        elif tree[node] == '/':
            tree[node] = int(tree[child[node][0]]) / int(tree[child[node][1]])
    print(f'#{tc} {int(tree[1])}')

