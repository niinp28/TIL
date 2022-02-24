light = input()

n = len(light)
light = list('N' + light)

cnt = 0
for i in range(1, n+1):
    if light[i] == 'Y':
        cnt += 1
        num = i
        while True:
            if num <= n:
                if light[num] == 'N':
                    light[num] = 'Y'
                elif light[num] == 'Y':
                    light[num] = 'N'
                num += i
            else:
                break
print(cnt)