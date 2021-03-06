# 바닥 공사

N = int(input())

d = [0] * 1000

d[0], d[1] = 1, 3
for i in range(2, N):
    # 1 * 2 , 2 * 2 덮개 선택하는 경우, 2 * 1 덮개 선택하는 경우
    d[i] = (d[i - 2] * 2 + d[i - 1] + 1) % 796796

print(d[N - 1])
