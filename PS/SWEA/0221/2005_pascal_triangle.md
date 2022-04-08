# 2005 파스칼의 삼각형

```python
import sys
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    # 파스칼의 삼각형 토대가 되는 2차원 배열
    arr = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            # 맨 앞과 맨 끝은 무조건 1
            if j == 0 or j == i:
                arr[i][j] = 1
            # 전 행의 두 요소를 더해서 숫자를 할당한다.
            else:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

    print(f'#{tc}')
    for lst in arr:  # 0이 아닌 요소만 리스트에 다시 담아서 언패킹 출력
        res = [num for num in lst if num]
        print(*res)
```

