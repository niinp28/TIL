```python
T = int(input())

for tc in range(1, T+1):

    N = int(input())
    nums = list(map(int,input().split()))
    res = 0

    for i in range(N-1, 0, -1) : # 범위의 끝 위치를 설정
        for j in range(0, i) : # 설정된 범위 안에서 순회
            if nums[j] > nums[j+1] : # 큰 값이 오른쪽으로 이동
                nums[j], nums[j+1] = nums[j+1], nums[j]

    res = nums[-1] - nums[0] # 오름차순이므로 제일 끝값에서 처음 값을 뺌


    print(f'#{tc} {res}')
```

