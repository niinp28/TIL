import sys
sys.stdin = open('forth.txt')

T = int(input())
for tc in range(1, T+1):
    code = input().split()
    op = ['+', '-', '*', '/']
    stack = []
    res = 0
    for elem in code:
        if elem == '.':
            if len(stack) == 1:
                res = stack[0]
            else:
                res = 'error'
        elif elem in op:
            if len(stack) > 1:
                a = int(stack.pop())
                b = int(stack.pop())
                if elem == '+':
                    stack.append(a+b)
                elif elem == '-':
                    stack.append(b-a)
                elif elem == '*':
                    stack.append(a*b)
                elif elem == '/':
                    stack.append(b//a)
            else:
                res = 'error'
                break
        else:
            stack.append(elem)
    print(f'#{tc} {res}')
