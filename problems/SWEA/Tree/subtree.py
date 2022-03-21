import sys
sys.stdin = open('subtree.txt')

def traverse(n):
    global cnt
    if n == 0:
        return
    cnt += 1
    traverse(left[n])
    traverse(right[n])

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    lst = list(map(int, input().split()))

    # E: 간선의 갯수, E+1: 노드의 갯수, E+2: 인덱싱 편의성을 위함
    left = [0] * (E+2)
    right = [0] * (E+2)

    # 트리에 노드 배치
    for i in range(0, len(lst), 2):
        if not left[lst[i]]:
            left[lst[i]] = lst[i+1]
        else:
            right[lst[i]] = lst[i+1]

    cnt = 0
    traverse(N)
    print(f'#{tc} {cnt}')
