import sys
sys.stdin = open('binary_heap.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(enumerate((map(int, input().split())), 1))
    tree = [0 for _ in range(N+1)]
    res = 0

    # tree에 숫자를 일단 배치한다
    for node, num in lst:
        tree[node] = num

    # 자리바꾸기
    for i in range(1, N+1):
        while tree[i//2] > tree[i]:  # 부모가 자식보다 클 때 바꾼다.
            tree[i//2], tree[i] = tree[i], tree[i//2]
            i = i // 2  # 다음 부모에 대해서도 검사한다.

    while N:
        res += tree[N//2]  # 부모 노드의 값을 더해준다
        N = N//2

    print(f'#{tc} {res}')
