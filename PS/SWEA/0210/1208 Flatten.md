```python
for tc in range(1, 11):
    N = int(input())
    heights = list(map(int, input().split()))

    for _ in range(N):
        max_H = heights[0] # 초기값 설정
        min_H = heights[0]
        for idx in range(len(heights)): # 최대, 최소 높이 찾기
            if max_H <= heights[idx]:
                max_H = heights[idx]
            if min_H >= heights[idx]:
                min_H = heights[idx]

        # 최대, 최소 높이에 해당하는 값의 인덱스 할당
        max_idx = heights.index(max_H)
        min_idx = heights.index(min_H)

        # 최대 높이는 한칸 감소, 최소 높이는 한칸 증가
        heights[max_idx] -= 1
        heights[min_idx] += 1

    max_final = heights[0]
    min_final = heights[0]
    for i in range(len(heights)):
        if max_final <= heights[i]:
            max_final = heights[i]
        if min_final >= heights[i]:
            min_final = heights[i]
    
    print(f'#{tc} {max_final - min_final}')
```

