import sys
sys.stdin = open('repeat.txt')
T = int(input())
for tc in range(1, T + 1):
    S = input()
    stack = ''
    for char in S:
        if len(stack) == 0:
            stack += char  # 스택이 비었으면 문자 추가
        else:  # 비어있지 않다면 top 과 해당 문자열 일치 검사
            if stack[-1] == char:
                stack = stack[:-1]  # 맨 끝 문자를 제외한 문자열로 재할당
            else:  # 같지 않다면 문자 추가
                stack += char
    print(f'#{tc} {len(stack)}')