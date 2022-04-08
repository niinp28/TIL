# Start 실습 - 단순 2진 암호코드(SWEA)

```python
import sys
sys.stdin = open('password.txt')
T = int(input())
pw_dict = {
    '0001101': '0',
    '0011001': '1',
    '0010011': '2',
    '0111101': '3',
    '0100011': '4',
    '0110001': '5',
    '0101111': '6',
    '0111011': '7',
    '0110111': '8',
    '0001011': '9'
}
for tc in range(1, T+1):
    N, M = map(int, input().split())
    for _ in range(N):  # 행을 내려오면서 입력을 한줄씩 받는다
        lst = input()
        if lst != '0' * M:  # 0만으로 이루어진 행이 아니라면
            pw_line = lst  # pw_line에 담는다

    for i in range(M-1, -1, -1):  # 뒤에서부터 순회하면서
        if pw_line[i] == '1':  # 1을 찾으면
            pw = pw_line[i-55: i+1]  # 56개의 숫자를 pw에 담는다
            break  # 그 뒤로 순회할 필요 없으므로 break

    real = ''
    for s in range(0, 56, 7):  # 10진수 숫자로 변환
        real += pw_dict[pw[s:s+7]]

    total = 0
    for idx in range(len(real)-1):  # 첫번째부터 7번째 자리까지 순회하면서
        if idx % 2:  # 짝수 자리는 그냥 더하고
            total += int(real[idx])
        else:  # 홀수 자리는 곱하기 3을 한 뒤 더한다.
            total += int(real[idx]) * 3

    res = 0
    if (total + int(real[-1])) % 10 == 0:  # 맞는 암호일 때
        for w in real:  # 모든 자리의 숫자를 더한다.
            res += int(w)
    else:  # 그렇지 않다면 0
        res = 0

    print(f'#{tc} {res}')
```

