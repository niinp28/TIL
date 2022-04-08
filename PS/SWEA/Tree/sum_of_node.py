T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    tree = [0 for _ in range(N + 1)]
    for _ in range(M):
        leaf, value = map(int, input().split())
        tree[leaf] = value

    # 노드 갯수가 0이라면 오른쪽 자식노드가 없으므로 0을 넣는다
    if not (N % 2):
        tree.append(0)

    # 노드 갯수가 4개 혹은 5개라면 [4+5, 2+3] 두 번의 덧셈이 일어난다
    # 6개 혹은 7개일 때: [6+7, 4+5, 2+3] 세 번의 덧셈이 일어난다
    # 따라서 왼쪽 자식 노드의 번호를 기준으로 인덱스를 잡아주었다.
    for i in range((N // 2) * 2, 1, -2):
        tree[i // 2] = tree[i] + tree[i + 1]

    print(f'#{tc} {tree[L]}')