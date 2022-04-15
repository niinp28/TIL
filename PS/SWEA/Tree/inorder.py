import sys
sys.stdin = open('inorder.txt')
def inorder(x):
    if x:
        inorder(left[x])
        print(tree[x], end='')
        inorder(right[x])

for tc in range(1, 11):
    N = int(input())
    tree = [0] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)
    for _ in range(N):
        tmp = input().split()
        tree[int(tmp[0])] = tmp[1]
        if tmp[2:]:
            left[int(tmp[0])] = int(tmp[2:][0])
            if tmp[3:]:
                right[int(tmp[0])] = int(tmp[2:][1])

    print(f'#{tc} ', end='')
    inorder(1)
    print()

